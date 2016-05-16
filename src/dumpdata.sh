#!/bin/sh
python manage.py dumpdata --natural-foreign --indent=2 \
  --exclude=admin.LogEntry \
  --exclude=auth.Permission \
  --exclude=axes \
  --exclude=captcha.CaptchaStore \
  --exclude=contenttypes \
  --exclude=dashboard.DashboardPreferences \
  --exclude=filebrowser \
  --exclude=sessions \
  --exclude=thumbnail.KVStore "$@"
