/*
 * Minimal read-side client for the governed-state API served by server/serve.py.
 *
 * Checkpoint 1 scope only: fetches ledger/ + memory/pending/ + decisions/ as read
 * from disk. Does not shape this into the console's `modules`/`actions` display
 * contract -- that mapping doesn't exist yet (ledger is currently empty, so there
 * is nothing to map against) and is explicitly a flagged, not assumed, next step.
 *
 * NOT wired into prototype/index.html. Load it explicitly where needed:
 *   <script src="../server/governed-client.js"></script>
 *   const state = await PiiGovernedData.load();
 */
(function (global) {
  'use strict';

  async function load(baseUrl) {
    const base = baseUrl || '';
    const res = await fetch(`${base}/api/state`);
    if (!res.ok) {
      throw new Error(`governed state fetch failed: HTTP ${res.status} ${res.statusText}`);
    }
    return res.json();
  }

  async function loadLedger(baseUrl) {
    const res = await fetch(`${baseUrl || ''}/api/ledger`);
    if (!res.ok) throw new Error(`ledger fetch failed: HTTP ${res.status}`);
    return (await res.json()).ledger;
  }

  async function loadPending(baseUrl) {
    const res = await fetch(`${baseUrl || ''}/api/pending`);
    if (!res.ok) throw new Error(`pending fetch failed: HTTP ${res.status}`);
    return (await res.json()).pending;
  }

  async function loadDecisions(baseUrl) {
    const res = await fetch(`${baseUrl || ''}/api/decisions`);
    if (!res.ok) throw new Error(`decisions fetch failed: HTTP ${res.status}`);
    return (await res.json()).decisions;
  }

  global.PiiGovernedData = { load, loadLedger, loadPending, loadDecisions };
})(typeof window !== 'undefined' ? window : globalThis);
