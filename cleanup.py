# Python program to demonstrate
# command line arguments
import argparse
# Initialize parser
parser = argparse.ArgumentParser()
# Adding optional argument
parser.add_argument("-ho","--host", help="The destination_path is required for connection to SFTP Server", required=True)
parser.add_argument("-u", "--username", help="The username is required for connection to SFTP Server.", required=True)
parser.add_argument("-p", "--password", help="The password is required for connection to SFTP Server.", required=True)
parser.add_argument("-dp", "--destination_path", help="The destination_path is required for connection to SFTP Server", required=True)


 
# Read arguments from command line
args = parser.parse_args()

if args:
    print("Displaying Output as: % s" % args.host)
    print("Displaying Output as: % s" % args.username)
    print("Displaying Output as: % s" % args.password)
    print("Displaying Output as: % s" % args.destination_path)
    
