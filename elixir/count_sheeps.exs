defmodule Shepherd do
  def count_sheeps_loop(cnt, []) do
    cnt
  end

  def count_sheeps_loop(cnt, [true | tail]) do
    count_sheeps_loop(cnt + 1, tail)
  end

  def count_sheeps_loop(cnt, [false | tail]) do
    count_sheeps_loop(cnt, tail)
  end

  def count_sheeps(sheeps) do
    count_sheeps_loop(0, sheeps)
  end
end

IO.puts(Shepherd.count_sheeps([true,  true,  true,  false,
true,  true,  true,  true ,
true,  false, true,  false,
true,  false, false, true ,
true,  true,  true,  true ,
false, false, true,  true]))

IO.puts("Hello world from Elixir")
