#!/usr/bin/osascript
-- Main flow
set currentlyPlayingTrack to getCurrentlyPlayingTrack()
return currentlyPlayingTrack

-- Method to get the currently playing track
on getCurrentlyPlayingTrack()
  tell application "Spotify"
    set currentArtist to artist of current track as string
    set currentTrack to name of current track as string
    set currentID to id of current track as string
    return currentID
  end tell
end getCurrentlyPlayingTrack
