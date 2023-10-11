#!/bin/sh

#sqlite3 ./var/books.db < ./share/books.sql
sqlite3 ./var/primary/fuse/books.db < ./share/books.sql
