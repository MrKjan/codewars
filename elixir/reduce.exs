# https://www.codewars.com/kata/550f22f4d758534c1100025a/train/elixir

#     NORTH
# WEST     EAST
#     SOUTH

defmodule Directions do
  def reduce(directions), do: loop([], directions)

  def loop(ret, []), do: ret |> Enum.reverse
  def loop(ret, ["NORTH", "SOUTH" | tail]), do: loop([], Enum.reverse(ret) ++ tail)
  def loop(ret, ["SOUTH", "NORTH" | tail]), do: loop([], Enum.reverse(ret) ++ tail)
  def loop(ret, ["WEST", "EAST" | tail]), do: loop([], Enum.reverse(ret) ++ tail)
  def loop(ret, ["EAST", "WEST" | tail]), do: loop([], Enum.reverse(ret) ++ tail)
  def loop(ret, [item | tail]), do: loop([item | ret], tail)
end

IO.puts Directions.reduce ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]