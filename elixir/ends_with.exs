defmodule EndsWith do
  def solution(_str, "") do
    true
  end

  def solution(str, ending) do
    String.slice(str, -String.length(ending)..-1) == ending
  end
end

IO.puts(EndsWith.solution("", "sdfg"))
