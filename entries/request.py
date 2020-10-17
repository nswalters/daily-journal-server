import sqlite3
import json

from models import Entry


def get_single_entry(id):
    with sqlite3.connect('../../dailyjournal.db') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.date,
            e.moodId
        FROM entries e
        WHERE e.id = ?
        """, (id, ))

        entries = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            entry = Entry(row['id'], row['concept'],
                          row['entry'], row['date'], row['moodId'])

            entries.append(entry.__dict__)

    return json.dumps(entries)


def get_all_entries():
    with sqlite3.connect("../../dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.date,
            e.moodId
        FROM entries e
        """)

        entries = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            entry = Entry(row['id'], row['concept'],
                          row['entry'], row['date'], row['moodId'])

            entries.append(entry.__dict__)

    return json.dumps(entries)


def delete_entry(id):
    with sqlite3.connect('../../dailyjournal.db') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM entries
        WHERE id = ?
        """, (id, ))


def get_entry_by_query(query):
    my_query = '%{}%'.format(query)

    with sqlite3.connect('../../dailyjournal.db') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.date,
            e.moodId
        FROM entries e
        WHERE e.entry LIKE ?
        """, (my_query,))

        entries = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            print(row)
            entry = Entry(row['id'], row['concept'],
                          row['entry'], row['date'], row['moodId'])

            entries.append(entry.__dict__)

    return json.dumps(entries)
