#!/usr/bin/osascript
-- Main flow
return getCurrentTime()

-- Method to get the currently playing track
on getCurrentTime()
  tell application "Spotify"
    set currentPos to player position as string
    return currentPos
  end tell
end getCurrentTime
