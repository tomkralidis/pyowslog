#!/usr/bin/python
# -*- coding: ISO-8859-15 -*-
# =================================================================
#
# Authors: Tom Kralidis <tomkralidis@hotmail.com>
#
# Copyright (c) 2011 Tom Kralidis
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# =================================================================

import sys
import fileinput
import re

from pyowslog.report import *

def usage():
    print '''
        Usage:
        
        %s <logfile> <ows_type> <ows_search_string> <skip_ip_list>'
        
        - logfile: path to httpd logfile (required)
        - ows_type: the type of OWS (possible values are OGC:WMS, OGC:WFS, OGC:WCS, OGC:SOS) (required)
        - ows_search_string: the URL path of the OWS to report on (e.g. /cgi-bin/wem_en) (required)
        - skip_ip_list: comma-separated list of IPs to skip (optional)
    ''' % sys.argv[0]

if len(sys.argv) < 4:
    usage()
    sys.exit(1)

if sys.argv[2] == 'OGC:WMS':
    s = WMSReport()
elif sys.argv[2] == 'OGC:WFS':
    s = WFSReport()
elif sys.argv[2] == 'OGC:WCS':
    s = WCSReport()
elif sys.argv[2] == 'OGC:SOS':
    s = SOSReport()
else:
    print 'Invalid ows_type (must be one of OGC:WMS, OGC:WFS, OGC:WCS, OGC:SOS)'
    usage()
    sys.exit(2)

resource = ''
resourceparam = ''
iplist = []

if len(sys.argv) == 5:
    iplist = sys.argv[4].split(',')

for line in fileinput.input(sys.argv[1]):
    if iplist:
        ip = re.compile('^(\S+)\s').search(line)
        if ip.group(1) in iplist:
            continue
    if line.find(sys.argv[3]) != -1:  # process the match
        # increment total hit count
        if line.find('POST') != -1:
            s.stats['operations']['POST']['hits'] += 1
        s.stats['hits'] += 1
        for k,v in s.stats['operations'].iteritems():
            if line.find(k) != -1:  # operation matched
                s.stats['operations'][k]['hits'] += 1
                if s.stats['operations'][k].has_key('resource'):  # resource matched
                    resource = k
                    resourceparam = s.stats['operations'][k]['resource']['param']
                    res = re.compile(s.stats['operations'][k]['resource']['param']+'=(\w+)\&', re.IGNORECASE).search(line)
                    if res is not None:
                        if s.stats['operations'][k]['resource']['list'].has_key(res.group(1)) is False:
                            s.stats['operations'][k]['resource']['list'][res.group(1)] = {}
                            s.stats['operations'][k]['resource']['list'][res.group(1)]['hits'] = 1
                        else:
                            s.stats['operations'][k]['resource']['list'][res.group(1)]['hits'] += 1

print "Total hits: ", s.stats['hits']

print "Total hits by request: "

for k, v in s.stats['operations'].iteritems():
  print ' ', k, v['hits']

if resource and resourceparam:
    print 'Total hits by ' + resource + ' ' + resourceparam + ': '
    for k, v in s.stats['operations'][resource]['resource']['list'].iteritems():
        print ' ', k, v['hits']

