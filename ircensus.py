#!/usr/bin/env python3

"""
A simple bot to gather some census data in IRC channels.

:author: tpltnt
:license: AGPLv3
"""
import irc.bot


class CensusBot(irc.bot.SingleServerIRCBot):
    pass

def main():
    import sys
    if len(sys.argv) != 4:
        print("Usage: " + sys.argv[0] + " <server[:port]> <channel> <nickname>")
        sys.exit(1)

    server = sys.argv[1].split(":", 1)
    host = server[0]
    if len(server) == 2:
        try:
            port = int(server[1])
        except ValueError:
            print("Error: Erroneous port.")
            sys.exit(1)
    else:
        port = 6667
    channel = sys.argv[2]
    nickname = sys.argv[3]

    print(port)
    bot = CensusBot(channel, nickname, server, port)
    bot.start()

if __name__ == "__main__":
    main()
