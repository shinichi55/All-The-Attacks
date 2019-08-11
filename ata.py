#!/usr/bin/python3

import pyattck
import argparse

parser = argparse.ArgumentParser (
    prog="all the attacks",
    description=""
)

parser.add_argument("tool", help="")

args = parser.parse_args()

attack = pyattck.Attck()

def tools():
    file = open( "ata.txt", "w" )

    for tool in attack.tools:
        if args.tool in tool.name:
            print( "Tool name: {}".format( tool.name ) )
            file.write( "Tool name: {}\n".format( tool.name ) )

            for actor in tool.actors:
                print( "Actor name/alias: {}".format( actor.aliases ))
                file.write( "Actor name/alias: {}\n".format( actor.aliases ) )
            
    file.close()

if __name__ == "__main__":
    tools()
