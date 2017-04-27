#!/usr/bin/osascript
-- Main flow
return getPlayerState()

-- Method to get the player state
on getPlayerState()
  tell application "Spotify"
    set playerState to player state as string
    return playerState
  end tell
end getPlayerState
