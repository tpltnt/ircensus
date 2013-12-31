#!/usr/bin/env python3

"""
A simple bot to gather some census data in IRC channels.
It is intended to sit in a channel and collect the data for statistics.

:author: tpltnt
:license: AGPLv3
"""
import irc.bot
import irc.strings
from irc.client import ip_numstr_to_quad, ip_quad_to_numstr


class CensusBot(irc.bot.SingleServerIRCBot):
    """
    The class implementing the census bot.
    """

    def __init__(self, channel, nickname, server, port=6667):
        """
        The constructor for the CensusBot class.

        :param channel: name of the channel to join
        :type channel: str
        :param nickname: nick of the bot (to use)
        :type nickname: str
        :param server: FQDN of the server to use
        :type server: str
        :param port: port to use when connecting to the server
        :type port: int
        """
        if 0 != channel.find('#'):
            channel = '#' + channel
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, nickname)
        self.channel = channel


    def on_nickname_in_use(self, connection, event):
        """
        Change own nickname if already in use.

        :param connection: connection to the server
        :type connection: irc.client.ServerConnection
        :param event: event to react to
        :type event: 
        :raises: TypeError
        """
        if not isinstance(connection, ServerConnection):
            raise TypeError("'connection' is not of type 'ServerConnection'")
        connection.nick(connection.get_nickname() + "_")


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

    bot = CensusBot(channel, nickname, server, port)
    bot.start()

if __name__ == "__main__":
    main()
