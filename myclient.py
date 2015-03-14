import argparse
import httplib

parser = argparse.ArgumentParser()
parser.add_argument("hostname", help="Enter a host name")
parser.add_argument("port", help="Enter a port number")
parser.add_argument("command", help="Enter GET or PUT")
parser.add_argument("filename", help="Enter a filename")
args = parser.parse_args()

a = args.hostname


if args.command == "GET":	
    conn = httplib.HTTPConnection(args.hostname,args.port)
    conn.request("GET", "/" + args.filename)
    resp = conn.getresponse()
    print resp.status, resp.reason
    data= resp.read()
    print data
    conn.close()
	
else:
    file = open(args.filename,"r")
    BODY = file.read()
    conn = httplib.HTTPConnection(args.hostname, args.port)
    conn.request("PUT", "/" + args.filename, BODY)
    response = conn.getresponse()
    print(response.status, response.reason)