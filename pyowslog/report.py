# -*- coding: ISO-8859-15 -*-
# =================================================================
#
# Authors: Tom Kralidis <tomkralidis@gmail.com>
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

class OWSReport(object):
    """Abstract report object"""
    def __init__(self):
        """spark up an instance"""
        self.stats = {}
        self.stats['hits'] = 0
        self.stats['operations'] = {}
        self.stats['operations']['GetCapabilities'] = {}
        self.stats['operations']['GetCapabilities']['hits'] = 0
        self.stats['operations']['POST'] = {}
        self.stats['operations']['POST']['hits'] = 0

class WMSReport(OWSReport):
    """WMS report object"""
    def __init__(self):
        """spark up an instance"""
        OWSReport.__init__(self)
        self.stats['type'] = 'OGC:WMS'
        self.stats['operations']['GetMap'] = {}
        self.stats['operations']['GetMap']['hits'] = 0
        self.stats['operations']['GetMap']['resource'] = {}
        self.stats['operations']['GetMap']['resource']['param'] = 'layers'
        self.stats['operations']['GetMap']['resource']['list'] = {}
        self.stats['operations']['GetFeatureInfo'] = {}
        self.stats['operations']['GetFeatureInfo']['hits'] = 0
        self.stats['operations']['GetLegendGraphic'] = {}
        self.stats['operations']['GetLegendGraphic']['hits'] = 0
        self.stats['operations']['GetStyles'] = {}
        self.stats['operations']['GetStyles']['hits'] = 0
        self.stats['operations']['DescribeLayer'] = {}
        self.stats['operations']['DescribeLayer']['hits'] = 0

class WFSReport(OWSReport):
    """WFS report object"""
    def __init__(self):
        """spark up an instance"""
        OWSReport.__init__(self)
        self.stats['type'] = 'OGC:WFS'
        self.stats['operations']['GetFeature'] = {}
        self.stats['operations']['GetFeature']['hits'] = 0
        self.stats['operations']['GetFeature']['resource'] = {}
        self.stats['operations']['GetFeature']['resource']['param'] = 'typename'
        self.stats['operations']['GetFeature']['resource']['list'] = {}
        self.stats['operations']['DescribeFeatureType'] = {}
        self.stats['operations']['DescribeFeatureType']['hits'] = 0

class WCSReport(OWSReport):
    """WCS report object"""
    def __init__(self):
        """spark up an instance"""
        OWSReport.__init__(self)
        self.stats['type'] = 'OGC:WCS'
        self.stats['operations']['GetCoverage'] = {}
        self.stats['operations']['GetCoverage']['hits'] = 0
        self.stats['operations']['GetCoverage']['resource'] = {}
        self.stats['operations']['GetCoverage']['resource']['param'] = 'coverage'
        self.stats['operations']['GetCoverage']['resource']['list'] = {}
        self.stats['operations']['DescribeCoverage'] = {}
        self.stats['operations']['DescribeCoverage']['hits'] = 0

class SOSReport(OWSReport):
    """SOS report object"""
    def __init__(self):
        """spark up an instance"""
        OWSReport.__init__(self)
        self.stats['type'] = 'OGC:SOS'
        self.stats['operations']['GetObservation'] = {}
        self.stats['operations']['GetObservation']['hits'] = 0
        self.stats['operations']['GetObservation']['resource'] = {}
        self.stats['operations']['GetObservation']['resource']['param'] = 'observedproperty'
        self.stats['operations']['GetObservation']['resource']['list'] = {}
        self.stats['operations']['DescribeSensor'] = {}
        self.stats['operations']['DescribeSensor']['hits'] = 0
