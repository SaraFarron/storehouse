from storehouse import db


def clear_data(session):
    # Maybe use
    # db.drop_all()
    # db.create_all()
    # db.session.commit()

    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print('Clear table %s' % table)
        session.execute(table.delete())
    session.commit()
