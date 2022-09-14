from PNR_Read_Operations import *
from PNR_Write_Operations import *

# Write Operations
# write_pnr("local-disk-361806","bigtable-ins-01","my-table")


# Read Operations
# filter_limit_row_regex('local-disk-361806','bigtable-ins-01','my-table')
# filter_limit_col_family_regex("local-disk-361806","bigtable-ins-01","my-table")
# filter_limit_col_qualifier_regex("local-disk-361806","bigtable-ins-01","my-table")
filter_value_regex("local-disk-361806","bigtable-ins-01","my-table")