defmodule Challenge do
  def loop([], []) do
    true
  end

  def loop([], _stack) do
    false
  end

  def loop([brace | tail], []) do
    if brace in ["(", "[", "{"] do
      loop(tail, [brace])
    else
      false
    end
  end

  def loop([brace | tail_brace], [head_stack | tail_stack]) do
    cond do
      brace in ["(", "[", "{"] -> loop(tail_brace, [brace, head_stack | tail_stack])
      head_stack <> brace in ["()", "[]", "{}"] -> loop(tail_brace, tail_stack)
      true ->
        false
    end
  end

  def valid_braces(braces) do
    loop(String.codepoints(braces), [])
  end
end

IO.puts(Challenge.valid_braces("[{}()]()(){{{{}}}}"))
# IO.puts("Kekekke")
# IO.puts(Challenge.valid_braces("()()"))
