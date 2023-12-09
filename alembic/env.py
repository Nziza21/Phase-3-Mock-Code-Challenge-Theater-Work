from alembic import context
from sqlalchemy import engine_from_config, pool
from lib.models import Base 

# Specify the database URL in the Alembic config
config = context.config
config.set_main_option('sqlalchemy.url', 'sqlite:///theater.db')  

# Attach the database engine to the Alembic config
engine = engine_from_config(
    config.get_section(config.config_ini_section),
    prefix='sqlalchemy.',
    poolclass=pool.NullPool,
)

# Attach your application's metadata to the Alembic config
target_metadata = Base.metadata

# Attach the metadata to the context
context.configure(
    engine=engine,
    target_metadata=target_metadata,
    compare_type=True, 
)