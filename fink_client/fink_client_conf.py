# Copyright 2019 AstroLab Software
# Author: Julien Peloton
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
""" Configuration file for the fink-client API.
"""
# Fink broker credentials. Contact us to get them.
username = "tarek"
password = None
group_id = "lsstfr-tarek"

# Timeout when polling alerts (seconds)
maxtimeout = 10

# Allow to overwrite alerts and loop over a subset of inputs
testmode = True

# List of topic names you subscribed to
# See https://fink-broker.readthedocs.io/en/latest/distribution/introduction/
# mytopics = ["rrlyr_workshop"]
mytopics = ["snialike_workshop"]

# Servers from which data will be pulled
servers = "134.158.74.95:24499,"

# Incoming alert schema to decode the data. You need to specify full path.
# If empty, the client will attempt to download the online latest version.
schema = "/Users/tallamjr/Github/fink-client/schemas/distribution_schema_0p2-live.avsc"

# Monitoring database. It includes metadata for the client to run.
# You need to specify the full path
# If it does not exist, it will be automatically created by the client.
db_path = '/Users/tallamjr/Github/fink-client/db/alert-monitoring.db'
