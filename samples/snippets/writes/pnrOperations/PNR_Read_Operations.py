



# [START bigtable_filters_print]
from google.cloud import bigtable
from JSONFileOperation import read_json
import google.cloud.bigtable.row_filters as row_filters
def print_row(row):
    print("Reading data for {}:".format(row.row_key.decode("utf-8")))
    for cf, cols in sorted(row.cells.items()):
        print("Column Family {}".format(cf))
        for col, cells in sorted(cols.items()):
            for cell in cells:
                labels = (
                    " [{}]".format(",".join(cell.labels)) if len(cell.labels) else ""
                )
                print(
                    "\t{}: {} @{}{}".format(
                        col.decode("utf-8"),
                        cell.value.decode("utf-8"),
                        cell.timestamp,
                        labels,
                    )
                )
    print("")

    
def getValues(row):
    l={}
    for cf, cols in sorted(row.cells.items()):
        for col_name, cells in sorted(cols.items()):
            for cell in cells:
                cell_value = cell.value.decode("utf-8")
                l[col_name]=cell_value 
    #             l[col_name]=cell.values()  
    # print(l)
    return l

# [END bigtable_filters_print]


# [START bigtable_filters_limit_row_regex]
def filter_limit_row_regex(project_id, instance_id, table_id):
    client = bigtable.Client(project=project_id, admin=True)
    instance = client.instance(instance_id)
    table = instance.table(table_id)

    rows = table.read_rows(
        filter_=row_filters.RowKeyRegexFilter(".*Raghav-r1$".encode("utf-8"))
    )
    
    for row in rows:
        print_row(row)
    
    
# filter_limit_row_regex('local-disk-361806','bigtable-ins-01','my-table')
# [END bigtable_filters_limit_row_regex]



# [START bigtable_filters_limit_col_family_regex]
def filter_limit_col_family_regex(project_id, instance_id, table_id):
    client = bigtable.Client(project=project_id, admin=True)
    instance = client.instance(instance_id)
    table = instance.table(table_id)

    rows = table.read_rows(
        filter_=row_filters.FamilyNameRegexFilter(".*cf1$".encode("utf-8"))
    )
    for row in rows:
        print_row(row)

# filter_limit_col_family_regex("local-disk-361806","bigtable-ins-01","my-table")
# [END bigtable_filters_limit_col_family_regex]




# [START bigtable_filters_limit_col_qualifier_regex]
def filter_limit_col_qualifier_regex(project_id, instance_id, table_id):
    client = bigtable.Client(project=project_id, admin=True)
    instance = client.instance(instance_id)
    table = instance.table(table_id)

    rows = table.read_rows(
        filter_=row_filters.ColumnQualifierRegexFilter(".*PNR02$".encode("utf-8"))
    )
    for row in rows:
        print_row(row)

# filter_limit_col_qualifier_regex("local-disk-361806","bigtable-ins-01","my-table")
# [END bigtable_filters_limit_col_qualifier_regex]




# [START bigtable_filters_limit_col_family_regex]

# def recursive_items(dictionary):
#     for key, value in dictionary.items():
#         if type(value) is dict:
#             yield from recursive_items(value)
#         else:
#             yield (key, value)


def filter_value_regex(project_id, instance_id, table_id):
    client = bigtable.Client(project=project_id, admin=True)
    instance = client.instance(instance_id)
    table = instance.table(table_id)

    rows = table.read_rows(
        filter_=row_filters.ValueRegexFilter(".*Raghav-dad.*".encode("utf-8"))
    )
    
    for row in rows:
        l = getValues(row)
    
    # for key, value in recursive_items(l):
    #     print("Key is: {} and Value is: {}".format(key,value))
    
    for v in l.values():
        s = eval(v)
        # print(s["Passenger-details"][0])  # Accessing child dictionary key
        for i in s['Passenger-details']:
            print("booking_id:", i['booking_id'])
            print("card_id:", i['card_id'])
            print("trip_name:", i['trip_name'])
            print("city_code:", i['city_code'])
            print("status:", i['status'])
            print("departure_date:", i['departure_date'])
            print("return_date:", i['return_date'])
            print("travellers:", i['travellers'])
            print()
        
  
            
        
# filter_value_regex("local-disk-361806","bigtable-ins-01","my-table")
# [END bigtable_filters_limit_col_family_regex]
