# https://www.codewars.com/kata/551dc350bf4e526099000ae5/train/elixir

defmodule SongDecoder do
  def decode_song(song) do
    song
    |> String.split("WUB", trim: true)
    |> Enum.join(" ")
  end
end

IO.puts SongDecoder.decode_song "WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"
