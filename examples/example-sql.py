import psycopg2

# MusicBrainz is an open music encyclopedia that collects
# music metadata and makes it available to the public.
# https://musicbrainz.org/doc/MusicBrainz_Database/Download
conn = psycopg2.connect("dbname=musicbrainz user=postgres")
cur = conn.cursor()

query = """
--begin-sql
SELECT
    a.gid,
    a.name,
    a.begin_date_year,
    a.end_date_year 
FROM artist AS a
WHERE 
    a.name='Ludwig van Beethoven'
--end-sql
"""

cur.execute(query)
first_row = cur.fetchone()
