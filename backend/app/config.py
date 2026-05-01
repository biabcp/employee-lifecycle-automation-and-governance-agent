import os
DATABASE_URL=os.getenv('DATABASE_URL','sqlite:///./lifecycle.db')
SECRET_KEY=os.getenv('SECRET_KEY','secret')
REDIS_URL=os.getenv('REDIS_URL','redis://localhost:6379/0')
