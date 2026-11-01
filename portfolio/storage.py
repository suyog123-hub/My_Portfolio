from whitenoise.storage import CompressedManifestStaticFilesStorage


class RelaxedManifestStorage(CompressedManifestStaticFilesStorage):
    # Don't crash the whole page when a static file is missing from the
    # manifest (e.g. a freshly added asset before `collectstatic` runs).
    # Fall back to the plain, unhashed URL instead of raising ValueError.
    manifest_strict = False
