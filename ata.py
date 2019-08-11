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
                print( "Actor name: {}".format( actor.name ) )
                file.write( "Actor name: {}\n".format( actor.name ) )

    file.close()

def actors():
    file = open( "ata.txt", "a" )
    act = input( "\nActor name to lookup: " )
    
    file.write( "\nActor name: {}\n".format( act ) )
    for actor in attack.actors:
        if act in actor.name:
            for technique in actor.techniques:
                print( technique.name )
                file.write( "{}\n".format( technique.name ) )
        else:
            continue

    file.close()

def technique():
    file = open( "ata.txt", "a" )
    mit = input( "\nTechnique to lookup: " )

    file.write( "\nTechnique name: {}\n".format( mit ) )
    for technique in attack.techniques:
        if mit in technique.name:
            for mitigation in technique.mitigation:
                print( mitigation.description )
                file.write( "{}\n".format( mitigation.description ) )
        else:
            continue
    
    file.close()

if __name__ == "__main__":
    tools()
    actors()
    technique()
