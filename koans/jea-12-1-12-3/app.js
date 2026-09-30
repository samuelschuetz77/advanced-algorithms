const sections = [
  { id: '12.1', title: 'A game you can’t win', short: 'Circuit satisfiability' },
  { id: '12.2', title: 'P versus NP', short: 'Solving & verifying' },
  { id: '12.3', title: 'Hardness & reductions', short: 'What must carry over' }
];

// Each koan has exactly one missing word. Sentences are paraphrases of the reading.
const koans = [
  { section: 0, before: 'A Boolean circuit combines AND, OR, and ', after: ' gates.', answer: 'NOT', hint: 'The gate that flips a Boolean value.', why: 'NOT reverses a Boolean input; the other named gates combine inputs.' },
  { section: 0, before: 'CircuitSat asks whether some input makes a circuit output ', after: '.', answer: 'true', hint: 'The output that makes the circuit satisfiable.', why: 'Circuit satisfiability is a yes/no question about whether any input produces True.' },
  { section: 0, before: 'An assignment that makes the output true is called a satisfying ', after: '.', answer: 'assignment', hint: 'It specifies a value for every input.', why: 'A satisfying assignment gives input values for which the circuit evaluates to True.' },
  { section: 0, before: 'With n binary switches, there are 2ⁿ possible ', after: '.', answer: 'settings', accepts: ['states', 'configurations', 'assignments', 'combinations', 'inputs'], hint: 'Each switch has two choices.', why: 'The number of possible input settings doubles with every new switch.' },
  { section: 0, before: 'Given one proposed input setting, evaluating the circuit is ', after: ' in its size.', answer: 'polynomial', accepts: ['linear'], hint: 'A standard notion of efficient running time.', why: 'A proposed setting can be checked efficiently by evaluating the circuit.' },
  { section: 0, before: 'Trying all 2ⁿ input settings takes ', after: ' time in n.', answer: 'exponential', hint: 'The variable n appears in the exponent.', why: 'Brute force explores exponentially many possible inputs.' },
  { section: 0, before: 'Whether CircuitSat has a polynomial-time algorithm is still ', after: '.', answer: 'unknown', accepts: ['open', 'unproven', 'not known', 'unkown', 'not knwon'], hint: 'No proof has settled this question.', why: 'No polynomial-time algorithm is known, but none has been proved impossible.' },
  { section: 0, before: 'One satisfying input can prove a “yes” answer, but the absence of one is harder to ', after: '.', answer: 'prove', hint: 'Think about what a short certificate could establish.', why: 'One successful input certifies yes; showing every input fails is a different challenge.' },

  { section: 1, before: 'A decision problem has a ', after: '-or-no answer.', answer: 'yes', hint: 'The affirmative answer.', why: 'P, NP, and co-NP are defined here as classes of decision problems.' },
  { section: 1, before: 'P contains decision problems that can be ', after: ' in polynomial time.', answer: 'solved', hint: 'The algorithm produces the answer itself.', why: 'Membership in P means there is a polynomial-time decision algorithm.' },
  { section: 1, before: 'NP contains decision problems whose yes answers have efficiently checkable ', after: '.', answer: 'proofs', accepts: ['certificates', 'witnesses'], hint: 'A proposed solution can serve as one.', why: 'For a yes instance in NP, a proof or certificate can be verified in polynomial time.' },
  { section: 1, before: 'NP emphasizes fast ', after: ' of a proposed yes answer.', answer: 'verification', hint: 'Checking a supplied candidate.', why: 'A yes certificate can be checked quickly even if finding one is difficult.' },
  { section: 1, before: 'A certificate is a proposed proof whose validity can be ', after: ' efficiently.', answer: 'checked', accepts: ['verified'], hint: 'A verifier tests the proposed proof.', why: 'A certificate lets us check a yes answer without finding it from scratch.' },
  { section: 1, before: 'For CircuitSat, a satisfying input is a yes ', after: '.', answer: 'certificate', accepts: ['witness', 'proof'], hint: 'Something you hand to a verifier.', why: 'The verifier evaluates the circuit on that input.' },
  { section: 1, before: 'In co-NP, a no answer has a polynomial-time checkable ', after: '.', answer: 'proof', accepts: ['certificate', 'witness'], hint: 'The counterpart to a yes certificate for NP.', why: 'co-NP gives efficient certificates for no instances.' },
  { section: 1, before: 'Every problem in P is also in ', after: '.', answer: 'NP', hint: 'You can verify a yes answer by solving again.', why: 'A polynomial-time solver also provides a polynomial-time verifier.' },
  { section: 1, before: 'For a problem in P, a ', after: ' answer can be verified by solving the problem again.', answer: 'no', blankChars: 3, hint: 'The kind of answer that co-NP certifies.', why: 'A polynomial-time solver can verify a no answer from scratch, so P is contained in co-NP.' },
  { section: 1, before: 'Whether P equals NP remains an ', after: ' question.', answer: 'open', accepts: ['unanswered', 'unresolved', 'unsolved', 'unsaswered'], hint: 'It has not been settled mathematically.', why: 'Most researchers expect P ≠ NP, but no proof is known.' },

  { section: 2, before: 'An NP-hard problem is at least as hard as ', after: ' problem in NP.', answer: 'every', hint: 'The definition ranges over the whole class.', why: 'If an NP-hard problem had a polynomial-time algorithm, every NP problem would too.' },
  { section: 2, before: 'A polynomial-time algorithm for any NP-hard problem would imply P = ', after: '.', answer: 'NP', hint: 'The other complexity class in the famous open question.', why: 'That is the consequence in Erickson’s definition of NP-hardness.' },
  { section: 2, before: 'A problem is NP-complete when it is NP-hard and belongs to ', after: '.', answer: 'NP', hint: 'Its yes answers can be verified efficiently.', why: 'NP-complete combines hardness with membership in NP.' },
  { section: 2, before: 'NP-hardness alone does not guarantee membership in ', after: '.', answer: 'NP', hint: 'Hardness and membership are separate claims.', why: 'NP-hard problems need not be NP-complete.' },
  { section: 2, before: 'In a hardness proof, the reduction transforms instances of a known hard problem into instances of the ', after: ' problem.', answer: 'target', hint: 'This is the problem whose hardness you want to prove.', why: 'The reduction runs from a known hard source toward the target problem.' },
  { section: 2, before: 'A many-one reduction maps a yes instance to a ', after: ' instance.', answer: 'yes', hint: 'It must keep the answer unchanged.', why: 'The transformed instance must have the same decision answer as the original.' },
  { section: 2, before: 'The same reduction must also map a no instance to a ', after: ' instance.', answer: 'no', hint: 'Preserve the other possible answer too.', why: 'The equivalence must work in both directions, for all inputs.' },
  { section: 2, before: 'A reduction used for NP-hardness must run in ', after: ' time.', answer: 'polynomial', hint: 'Its overhead must remain efficient.', why: 'An exponential transformation would not transfer a polynomial-time solver back to the source.' },
  { section: 2, before: 'To prove NP-completeness, establish both NP-hardness and NP ', after: '.', answer: 'membership', hint: 'Show that the target itself belongs to NP.', why: 'A hardness reduction alone proves only the hardness half.' }
];

const storageKey = 'jea-complexity-koans-v4';
const storedIndex = Number(localStorage.getItem(storageKey));
let index = Number.isInteger(storedIndex) && storedIndex < koans.length
  ? Math.max(0, storedIndex)
  : 0;
let advancing = false;
let advanceTimer;

const form = document.querySelector('#answer-form');
const sentence = document.querySelector('#sentence');
const feedback = document.querySelector('#feedback');
const normalize = value => value.trim().toLocaleLowerCase();

function render() {
  advancing = false;
  if (index === koans.length) {
    sentence.textContent = 'Complete.';
    feedback.textContent = '';
    return;
  }
  const koan = koans[index];
  const input = document.createElement('input');
  input.id = 'answer';
  input.type = 'text';
  input.inputMode = 'text';
  input.autocomplete = 'off';
  input.spellcheck = false;
  if (koan.blankChars) input.style.width = `${koan.blankChars}ch`;
  input.setAttribute('aria-label', 'Missing word');
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
    feedback.textContent = 'Try another word.';
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
