import os
import sqlite3
from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Domain(Base):
    __tablename__ = 'domains'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False, index=True)
    title = Column(String(150), nullable=False)
    total_endpoints = Column(Integer, default=0)

    categories = relationship('Category', back_populates='domain', cascade='all, delete-orphan')
    endpoints = relationship('Endpoint', back_populates='domain', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Domain(name='{self.name}', title='{self.title}', count={self.total_endpoints})>"


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    domain_id = Column(Integer, ForeignKey('domains.id'), nullable=False, index=True)
    name = Column(String(150), nullable=False, index=True)
    slug = Column(String(150), nullable=False)

    domain = relationship('Domain', back_populates='categories')
    endpoints = relationship('Endpoint', back_populates='category', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Category(name='{self.name}')>"


class Endpoint(Base):
    __tablename__ = 'endpoints'

    id = Column(Integer, primary_key=True)
    domain_id = Column(Integer, ForeignKey('domains.id'), nullable=False, index=True)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False, index=True)
    section_number = Column(String(50), nullable=False, index=True)
    title = Column(String(255), nullable=False)
    method = Column(String(10), nullable=False, index=True)
    path = Column(String(255), nullable=False, index=True)
    summary = Column(Text, nullable=True)
    required_scopes = Column(Text, nullable=True)
    doc_filepath = Column(String(255), nullable=False)
    start_line = Column(Integer, nullable=False)
    end_line = Column(Integer, nullable=False)

    domain = relationship('Domain', back_populates='endpoints')
    category = relationship('Category', back_populates='endpoints')

    def __repr__(self):
        return f"<Endpoint(section='{self.section_number}', method='{self.method}', path='{self.path}')>"


def get_default_db_path():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    data_dir = os.path.join(base_dir, 'data')
    os.makedirs(data_dir, exist_ok=True)
    return os.path.join(data_dir, 'webex_docs.db')


def get_engine(db_path=None):
    if not db_path:
        db_path = get_default_db_path()
    return create_engine(f"sqlite:///{db_path}", echo=False)


def get_session(engine=None):
    if not engine:
        engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()


def init_db(db_path=None):
    if not db_path:
        db_path = get_default_db_path()

    engine = get_engine(db_path)
    Base.metadata.create_all(engine)

    # Initialize SQLite FTS5 Virtual Table for full-text search
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute('''
    CREATE VIRTUAL TABLE IF NOT EXISTS endpoints_fts USING fts5(
        domain_name,
        category_name,
        title,
        method,
        path,
        summary
    )
    ''')
    conn.commit()
    conn.close()
    return engine
