// Based on projects or assignments i turn in live here/max_flow.py.
// The BFS version is the main thread; the other five explore path choices.
const koans = [
  // Flow and capacity
  { section: 'flow', before: 'In capacity[u][v], the number is the most flow edge u → v can ', after: '.', answer: 'carry' },
  { section: 'flow', before: 'At an intermediate vertex, total inflow must equal total ', after: '.', answer: 'outflow' },
  { section: 'flow', code: 'capacity = {"s": {"a": 7}, "a": {"t": 4}}', before: 'Even though s → a holds 7, this single route can send at most ', after: ' units to t.', answer: '4' },
  { section: 'flow', before: 'The value of a flow is the net amount leaving the ', after: '.', answer: 'source' },
  { section: 'flow', before: 'An augmenting path needs positive residual room on every ', after: '.', answer: 'edge' },

  // Residual graph and augmentation
  { section: 'residual', code: 'residual[u][v] = capacity[u][v]', before: 'Initially, the forward residual room equals the edge’s ', after: '.', answer: 'capacity' },
  { section: 'residual', before: 'The code builds a separate residual graph so updates do not change the original ', after: ' graph.', answer: 'capacity' },
  { section: 'residual', code: 'if u not in residual[v]:\n    residual[v][u] = 0', before: 'A missing reverse edge starts with residual room ', after: '.', answer: '0', accepts: ['zero'] },
  { section: 'residual', code: 'capacity = {"s": {"a": 5}, "a": {"s": 2}}', before: 'Because a → s is an original edge, its initial residual room is ', after: '.', answer: '2' },
  { section: 'residual', code: 's → a: 5\na → t: 2', before: 'The bottleneck of this path is ', after: '.', answer: '2' },
  { section: 'residual', code: 'residual[u][v] = 5\namount = 2\nresidual[u][v] -= amount', before: 'After this update, the forward residual room is ', after: '.', answer: '3' },
  { section: 'residual', code: 'residual[v][u] = 0\namount = 2\nresidual[v][u] += amount', before: 'The reverse edge can now undo ', after: ' units of earlier flow.', answer: '2' },

  // Edmonds-Karp BFS
  { section: 'bfs', code: 'queue = deque([source])\nu = queue.popleft()', before: 'Removing from the front makes this search ', after: '-first.', answer: 'breadth' },
  { section: 'bfs', code: 'parent[v] = u', before: 'This records the vertex immediately before v on the discovered ', after: '.', answer: 'path' },
  { section: 'bfs', code: 'if room > 0 and v not in parent:', before: 'An edge with zero residual room cannot be ', after: '.', answer: 'traversed', accepts: ['used', 'followed'] },
  { section: 'bfs', before: 'BFS finds an augmenting path with the fewest ', after: ', regardless of capacities.', answer: 'edges' },
  { section: 'bfs', code: 'if sink not in parent:\n    return total', before: 'With no residual path to the sink, the current flow is ', after: '.', answer: 'maximum', accepts: ['optimal'] },

  // Stack DFS and recursive DFS
  { section: 'dfs', code: 'stack = [source]\nu = stack.pop()', before: 'Removing the newest item gives a depth-first ', after: '.', answer: 'search', accepts: ['traversal'] },
  { section: 'dfs', code: 'if u == sink:\n    return True', before: 'The recursive search succeeds when it reaches the ', after: '.', answer: 'sink' },
  { section: 'dfs', code: 'if room > 0 and v not in parent:', before: 'The parent check prevents revisiting a vertex and getting stuck in a ', after: '.', answer: 'cycle', accepts: ['loop'] },
  { section: 'dfs', before: 'BFS and DFS may pick different paths, but each successful path increases the total ', after: '.', answer: 'flow' },

  // Widest path and capacity scaling
  { section: 'widest', code: 'width = min(path_width, room)', before: 'The width of a path is limited by its ', after: ' edge.', answer: 'smallest', accepts: ['narrowest', 'minimum'] },
  { section: 'widest', code: 'heappush(heap, (-width, next(sequence), v))', before: 'Negating width makes Python’s min-heap remove the ', after: ' width first.', answer: 'largest', accepts: ['greatest', 'maximum'] },
  { section: 'widest', before: 'Widest-path search prefers the route that can carry the most flow in one ', after: '.', answer: 'augmentation', accepts: ['step', 'push'] },
  { section: 'scaling', code: 'largest = 13\nscale = 1\nwhile scale * 2 <= largest:\n    scale *= 2', before: 'The first capacity threshold is ', after: '.', answer: '8' },
  { section: 'scaling', code: 'if room >= scale:', before: 'At scale 8, an edge with residual room 7 is ', after: '.', answer: 'skipped', accepts: ['ignored', 'excluded'] },
  { section: 'scaling', before: 'Reducing the threshold down to 1 lets scaling use every positive ', after: ' capacity.', answer: 'integer' },

  // Dinic
  { section: 'dinic', code: 'level[v] = level[u] + 1', before: 'The level records distance from the source in number of ', after: '.', answer: 'edges' },
  { section: 'dinic', code: 'level.get(v) == level[u] + 1', before: 'Dinic’s DFS moves only to the ', after: ' level.', answer: 'next' },
  { section: 'dinic', before: 'A blocking flow leaves every source-to-sink route in the current level graph with a ', after: ' edge.', answer: 'saturated', accepts: ['full'] }
];

const storageKey = 'max-flow-koans-v1';
const storedIndex = Number(localStorage.getItem(storageKey));
let index = Number.isInteger(storedIndex) && storedIndex >= 0 && storedIndex <= koans.length
  ? storedIndex : 0;
let advancing = false;
let advanceTimer;

const form = document.querySelector('#answer-form');
const sentence = document.querySelector('#sentence');
const code = document.querySelector('#code');
const feedback = document.querySelector('#feedback');
const normalize = value => value.trim().toLocaleLowerCase();

function render() {
  advancing = false;
  if (index === koans.length) {
    code.hidden = true;
    sentence.textContent = 'Complete.';
    feedback.textContent = '';
    return;
  }

  const koan = koans[index];
  code.hidden = !koan.code;
  code.textContent = koan.code || '';
  const input = document.createElement('input');
  input.id = 'answer';
  input.type = 'text';
  input.inputMode = 'text';
  input.autocomplete = 'off';
  input.spellcheck = false;
  if (koan.answer.length <= 3) input.style.width = '4ch';
  input.setAttribute('aria-label', 'Missing word or number');
  input.setAttribute('aria-describedby', 'feedback');
  sentence.replaceChildren(document.createTextNode(koan.before), input, document.createTextNode(koan.after));
  feedback.textContent = '';
  input.focus();
}

function check(showWrong = false) {
  if (advancing || index === koans.length) return;
  const input = document.querySelector('#answer');
  const koan = koans[index];
  const value = normalize(input.value);
  const accepted = [koan.answer, ...(koan.accepts || [])].map(normalize);
  if (accepted.includes(value)) {
    advancing = true;
    input.classList.remove('wrong');
    input.classList.add('correct');
    input.disabled = true;
    feedback.textContent = 'Correct.';
    advanceTimer = window.setTimeout(() => {
      index += 1;
      localStorage.setItem(storageKey, String(index));
      render();
    }, 750);
  } else if (showWrong && value) {
    input.classList.add('wrong');
    feedback.textContent = 'Try another word or number.';
  }
}

form.addEventListener('input', () => {
  document.querySelector('#answer').classList.remove('wrong');
  feedback.textContent = '';
  check();
});
form.addEventListener('submit', event => {
  event.preventDefault();
  check(true);
});
document.querySelector('#restart-button').addEventListener('click', () => {
  window.clearTimeout(advanceTimer);
  index = 0;
  localStorage.setItem(storageKey, '0');
  render();
});
render();
