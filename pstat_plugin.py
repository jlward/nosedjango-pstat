import string
import math
import random
import logging

from nosedjango.plugins.base_plugin import Plugin

class PstatPlugin(Plugin):

    name = 'pstat'

    def beforeTestSetup(self, settings, setup_test_environment, connection):
        logging.getLogger().setLevel(logging.WARNING)
        switched_settings = {
            'DOCUMENT_IMPORT_STORAGE_DIR': 'document_import%(token)s',
            'DOCUMENT_SETTINGS_STORAGE_DIR': 'document_settings%(token)s',
            'ATTACHMENT_STORAGE_PREFIX': 'attachments%(token)s',
            'MAILER_LOCKFILE': 'send_mail%(token)s',
        }
        settings.DOCUMENT_PRINTING_CACHE_ON_SAVE = False

        from pstat.printing.conf import settings as print_settings
        from pstat.document_backup.conf import settings as backup_settings
        token = self.get_unique_token()
        print_settings.PDF_STORAGE_DIR = 'unittest/pdf_cache%s/' % token
        print_settings.PDF_STORAGE_BASE_URL = 'unittest/pdf_cache%s/' % token
        backup_settings.STORAGE_DIR = 'unittest/document_backup%s/' % token
        backup_settings.STORAGE_BASE_URL = 'unittest/document_backup%s/' % token

        for key, value in switched_settings.items():
            setattr(settings, key, value % {'token': token})
        settings.CACHE_BACKEND = 'locmem://'
        settings.DISABLE_QUERYSET_CACHE = True

        from django.core.cache import cache
        cache.clear()
