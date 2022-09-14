#!/usr/bin/env python

# Copyright 2019, Google LLC
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START bigtable_writes_simple]
import datetime
from google.cloud import bigtable
from JSONFileOperation import read_json

def write_pnr(project_id, instance_id, table_id):
    client = bigtable.Client(project=project_id, admin=True)
    instance = client.instance(instance_id)
    table = instance.table(table_id)

    timestamp = datetime.datetime.utcnow()
    # column_family_id = "stats_summary"
    column_family_id = "cf1"

    row_key = "Raghav-r1"
    
    pnr01_val= str(read_json('C://Users//asahu23//OneDrive - DXC Production//Desktop//TBJ//BigtableProject//samples//snippets//writes//pnrOperations//Raghav-PNR-01.json'))
    pnr02_val= str(read_json('C://Users//asahu23//OneDrive - DXC Production//Desktop//TBJ//BigtableProject//samples//snippets//writes//pnrOperations//Raghav-PNR-02.json'))
    pnr03_val= str(read_json('C://Users//asahu23//OneDrive - DXC Production//Desktop//TBJ//BigtableProject//samples//snippets//writes//pnrOperations//Raghav-PNR-03.json'))


    row = table.direct_row(row_key)
    row.set_cell(column_family_id, "PNR01", pnr01_val, timestamp)
    row.set_cell(column_family_id, "PNR02", pnr02_val, timestamp)
    row.set_cell(column_family_id, "PNR03", pnr03_val, timestamp)

    row.commit()

    print("Successfully wrote row {}.".format(row_key))

# write_pnr("local-disk-361806","bigtable-ins-01","my-table")

# [END bigtable_writes_simple]


