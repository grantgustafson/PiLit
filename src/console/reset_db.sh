#!/bin/bash

SCHEMA_FILE='schema/db.sql'
DB='db.db'

python db_schema.py > $SCHEMA_FILE
cat $SCHEMA_FILE

if [ -f $DB ]; then rm $DB; fi

sqlite3 $DB < $SCHEMA_FILE
