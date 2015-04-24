import data


class cohort:



    def __init__(self):

        self.data = None
        self.cohort_name = ""
        self.provenance_list = []
        self.filter = {}


    def data_init( self, filename ):

        self.data = data.Data( filename )
        ind = self.data.header2data["PROVENANCE"]

        self.provenance_list = self.data.get_column("PROVENANCE")
        self.prepareProvenance()
        
    def prepareProvenance(self):
        for word in self.provenance_list:
            temp = word.split("|")
            for new in temp:
                if(self.filter.has_key(new) == False):
                    self.filter[new] = 1
        self.provenance_list = self.filter.keys()
        # print(self.provenance_list)
                    

        # self.provenance_list = 

    def identify_cohorts( self ):

        if self.data != None:

            if not self.data.header2data.has_key("COHORT"):
                self.data.add_column( "COHORT" )

            cohortind = self.data.header2data[ "COHORT" ]
            provind = self.data.header2data["PROVENANCE"]  # in GUI this will be a user string

            for i in range( self.data.get_num_rows() ):
                pro = self.data.data[i][provind]
                #pro.upper()
                coh = self.data.data[i][cohortind]
                #coh.upper()
                delin = "|"
                for j in range( len( self.provenance_list ) ):
                    sub = self.provenance_list[j]
                    #sub.upper()

                    if coh.find( self.cohort_name ) > -1:
                        break

                    if pro.find( sub ) > -1:
                        self.data.set_value( i, "PROVENANCE", pro + "|" + self.cohort_name )
                        if coh == "":
                            delin = ""
                        self.data.data[i][cohortind] = self.data.data[i][cohortind] + delin + self.cohort_name

                        break


            self.data.save()

# test = cohort()

# test.data_init( 'schoenbergAll.csv' )
# test.cohort_name = 'pancakes'
# test.provenance_list =['Beck', 'watson']
# test.identify_cohorts(  )
