# go to https://developers.facebook.com/tools/explorer/ to obtain and set permissions for an access token
# Make sure the app has the appropriate permissions
# get your access token: # access toke: https://www.facebook.com/dialog/oauth?client_id=464891386855067&redirect_uri=https://www.facebook.com/connect/login_success.html&scope=basic_info,email,public_profile,user_about_me,user_activities,user_birthday,user_education_history,user_friends,user_interests,user_likes,user_location,user_photos,user_relationship_details&response_type=token
# make sure you have the html file in the same location
print "Please paste the FB access token, which can be retrieved here: https://www.facebook.com/dialog/oauth?client_id=464891386855067&redirect_uri=https://www.facebook.com/connect/login_success.html&scope=basic_info,email,public_profile,user_about_me,user_activities,user_birthday,user_education_history,user_friends,user_interests,user_likes,user_location,user_photos,user_relationship_details&response_type=token", "\n\n"
ACCESS_TOKEN = raw_input()
print "Thanks :)", "\n"

import requests # pip install requests
import json
import facebook # pip install facebook-sdk
import networkx as nx # pip install networkx
import requests # pip install requests
import time
from networkx.readwrite import json_graph
# from IPython.display import IFrame -> for rendering in ipython notebook
# from IPython.core.display import display -> for rendering in ipython notebook

print "done importing modules...", "\n"

startTime = time.time()

base_url = 'https://graph.facebook.com/me'

fields = 'id,name,friends'

url = '%s?fields=%s&access_token=%s' % \
    (base_url, fields, ACCESS_TOKEN,)

g = facebook.GraphAPI(ACCESS_TOKEN)

print "Authenticated Successfully", "\n"

print "this is the the stuff i'm pulling from facebook graph API: ", url, "\n"

content = requests.get(url).json()

friends = [ (friend['id'], friend['name'],)
                for friend in g.get_connections('me', 'friends')['data'] ]

url = 'https://graph.facebook.com/me/mutualfriends/%s?access_token=%s'

mutual_friends = {}

for friend_id, friend_name in friends:
    r = requests.get(url % (friend_id, ACCESS_TOKEN,) )
    response_data = json.loads(r.content)['data']
    mutual_friends[friend_name] = [ data['name']
                                    for data in response_data ]

nxg = nx.Graph()

[ nxg.add_edge('me', mf) for mf in mutual_friends ]

[ nxg.add_edge(f1, f2)
  for f1 in mutual_friends
      for f2 in mutual_friends[f1] ]

cliques = [c for c in nx.find_cliques(nxg)]

num_cliques = len(cliques)

clique_sizes = [len(c) for c in cliques]
max_clique_size = max(clique_sizes)
avg_clique_size = sum(clique_sizes) / num_cliques

max_cliques = [c for c in cliques if len(c) == max_clique_size]

num_max_cliques = len(max_cliques)

max_clique_sets = [set(c) for c in max_cliques]
friends_in_all_max_cliques = list(reduce(lambda x, y: x.intersection(y),
                                  max_clique_sets))
print "analyzed cliques...", "\n"

nld = json_graph.node_link_data(nxg)

json.dump(nld, open('force.json','w'))

# for use in ipython notebook:

# viz_file = 'fb-redirected.html'
# other viz_file = 'sticky.html'
# this is WIP, working on adding the persons name which is not working for some reason
#display(IFrame(viz_file, '100%', '1200px'))


print "Done in ", (time.time()-startTime), "seconds."
