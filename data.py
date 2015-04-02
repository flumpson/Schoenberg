# Erin Lavoie
# CS251
# Project 2

import csv
import sys
import numpy as np
import random as r

class Data:

    def __init__( self, filename = None ):

        #fields
        self.headers = []
        self.data = []
        self.header2data = {}

        #read in a file if provided
        if ( filename != None ):
            self.file = filename
            self.readData()

    #reads the data from a file
    def readData( self ):

        #read the file lines
        fp = file( self.file, "rU" )
        lines = fp.readlines()
        fp.close()

        #create a csv object
        csvr = csv.reader( lines )

        #set raw_headers to first line
        self.headers = csvr.next()

        for i in range( len( self.headers ) ):
            self.headers[i] = self.headers[i].strip()

        # loop through the rest of csvr and append each list to raw_data
        for thing in csvr:
            self.data.append( thing )

        # loop through the headers and k,v pair them w/ the corresponding index
        c = 0
        for i in range( len( self.headers ) ):
            self.header2data[ self.headers[ i ] ] = c
            c += 1

    # returns a list of the raw headers
    def get_headers( self ):

        return self.headers


    # returns the number of raw columns
    def get_num_columns( self ):

        return len( self.headers )

    # returns the number of rows
    def get_num_rows( self ):

        return len( self.data )

    # returns a row of raw data with the specified row number
    def get_row( self, rowNum ):

        return self.data[ rowNum ]

    # returns a column of data with the specified header string
    def get_column( self, header ):
        # list to column values
        col = []

        # header index
        ind = self.header2data.get( header )

        # adding data to column list
        for row in self.data:
            col.append( row[ind] )

        return col

    # returns the raw data at the given header, with the given row number
    def get_value( self, rowNum, header ):

        return self.data[ rowNum ][ self.header2data.get( header ) ]

    # sets the value at the given header, with the given row number
    def set_value( self, rowNum, header, value ):

        self.data[ rowNum ][ self.header2data.get( header ) ] = value

    # adds a column to the data set require a header, a type, and the correct number of points
    def add_column( self, header, plist = None ):

        # adding header to list of headers
        self.headers.append( header )

        # initializing counter
        c = 0
        # loop through raw data
        for row in self.data:
            if plist != None:
                # appending data to end of row
                row.append( plist[c] )
                c += 1 # incrementing counter
            else:
                row.append( "" )

        # adding entry to headers2raw dictionary
        self.header2data[ header ] = len( self.headers ) - 1

    def save( self, filename = None ):
        if filename == None:
            filename = self.file

        with open(filename, 'wb') as csvfile:
            writer = csv.writer(csvfile, dialect = 'excel')
            writer.writerow( self.headers )
            for row in self.data:
                writer.writerow( row )


    # prints the raw data
    def printData( self ):

        print self.headers
        for thing in self.data:
            print thing


if __name__ == "__main__":

    test = Data( sys.argv[1] )

    print "\n------------------------\ntesting header accesors: \n"
    print test.get_headers()

    print "\n------------------------\ntesting num_cols and num_rows: \n"
    print test.get_num_columns()
    print test.get_num_rows()

    print "\n------------------------\ntesting row accesor: \n"
    print test.get_row(2)

    print "\n------------------------\ntesting get_value and get_raw_value: \n"
    print test.get_value( 2, test.get_headers()[0] )

    print "\n------------------------\ntesting printData: \n"
    #print test.printData()



    print "\n\n--------------------------------------------------------\n\n"
    print "testing add column function"
    l = []
    for i in range(test.get_num_rows()):
        l.append(r.randint(0, 100))
    test.add_column("numeric", l)

    print "\n------------------------\ntesting header accesors: \n"
    print test.get_headers()

    print "\n------------------------\ntesting num_cols and num_rows: \n"
    print test.get_num_columns()

    print "\n------------------------\ntesting row accesor: \n"
    print test.get_row( test.get_num_columns() - 1 )

    print "\n------------------------\ntesting get_value and get_raw_value: \n"
    print test.get_value( 31, test.get_headers()[0] )

    print "\n------------------------\ntesting get_column: \n"
    #print test.get_column( "PROVENANCE" )
