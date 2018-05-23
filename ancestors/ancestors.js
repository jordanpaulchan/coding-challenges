function getAncestors(child, ancestors, personMap) {
  for (let parent of personMap.get(child)) {
    if (!ancestors.has(parent)) {
      ancestors.set(
        parent,
        ancestors.has(child) ? ancestors.get(child) + 1 : 0
      );
      getAncestors(parent, ancestors, personMap);
    }
  }
}

function checkAncestors(child1, child2) {
  for (let [ancestor, val] of child1) {
    if (child2.has(ancestor)) {
      return true;
    }
  }
  return false;
}

function shareAncestor(pairs, child1, child2) {
  const personMap = parentChildRelationships(pairs);
  const child1Ancestors = new Map();
  const child2Ancestors = new Map();
  getAncestors(child1, child1Ancestors, personMap);
  getAncestors(child2, child2Ancestors, personMap);

  return checkAncestors(child1Ancestors, child2Ancestors);
}

function parentChildRelationships(pairs) {
  const personMap = new Map();
  pairs.forEach(([parent, child]) => {
    if (!personMap.has(parent)) {
      personMap.set(parent, []);
    }

    if (!personMap.has(child)) {
      personMap.set(child, [parent]);
    } else {
      personMap.get(child).push(parent);
    }
  });

  return personMap;
}

const parentChildPairs = [
  [1, 3],
  [2, 3],
  [3, 6],
  [5, 6],
  [5, 7],
  [4, 5],
  [4, 8],
  [8, 9],
  [6, 10]
];

console.log(shareAncestor(parentChildPairs, 8, 9));
