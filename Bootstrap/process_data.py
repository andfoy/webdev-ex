#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
import sys
import codecs

contact = """
            <div class="student-container">
                <h2>%s</h2>  <!--name-->
                <h3>%s</h3>  <!--id-->
                <div class="contact-info">
                    <div class="contact-buttons btn-group">
                        <div class="row">
                            <div class="col-md-4">
                                <a class="custom-btn" href="%s"><i class="fa fa-github"></i> Github </a>
                            </div>
                            <div class="col-md-4">
                                <a class="custom-btn" href="https://twitter.com/%s"><i class="fa fa-twitter"></i> Twitter </a>
                            </div>
                            <div class="col-md-4">
                                <a class="custom-btn" href="mailto:%s"><i class="fa fa-envelope"></i> Mail </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
"""

container = """
        <div class="col-md-3">
"""

closing = """
        </div>
"""

cols = [[container] for _ in range(0, 4)]
idx = 0

with codecs.open('data.csv', 'rb', 'utf-8') as fp:
    lines = fp.readlines()

lines = map(lambda x: x.rstrip().split(','), lines)
header = lines[0]
lines = lines[1:]

for line in lines:
    info = dict(zip(header, line))
    if info['twitter'][0] == '@':
        info['twitter'] = info['twitter'][1:]
    result = contact % (info['name'], info['id'], info['github'],
                        info['twitter'], info['email'])
    cols[idx].append(result)
    idx = (idx + 1) % 4

cols = [col+[closing] for col in cols]
cols = ['\n'.join(col) for col in cols]
text = '\n'.join(cols)

with codecs.open('output.html', 'wb', 'utf-8') as fp:
    fp.write(text)