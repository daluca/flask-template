"""Flask configuration."""


class Config:
    """Base configuration accross all environments."""

    JSONIFY_PRETTYPRINT_REGULAR = True


class ProductionConfig(Config):
    """Set configuration for production environment."""

    pass


class StagingConfig(Config):
    """Set configuration for staging environment."""

    pass


class DevelopmentConfig(Config):
    """Set configuration for development environment."""

    pass


class TestingConfig(Config):
    """Set configuration for testing environment."""

    TESTING = True


config_map = {
    "production": ProductionConfig,
    "staging": StagingConfig,
    "development": DevelopmentConfig,
    "testing": TestingConfig
}
