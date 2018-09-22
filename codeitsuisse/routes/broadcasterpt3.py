import networkx as nx
import logging
from flask import request, jsonify;
from codeitsuisse import app;


logger = logging.getLogger(__name__)
@app.route('/broadcaster/fastest-path', methods=['POST','GET'])
def evaluate_fastest_path():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    node_list = data.get("data");
    sender = data.get("sender");
    recipient = data.get("recipient");
    nlist = []
    G = nx.Graph()
    for x in node_list:
        (a, d) = x.split('->')
        (b, c) = d.split(',')
        c = int(c)
        nlist.append([a,b,c])
    G.add_weighted_edges_from(nlist)
    z = nx.dijkstra_path(G, sender, recipient)
    result = {"result": z}
    print("Output Data:", result)
    logging.info("My result :{}".forms