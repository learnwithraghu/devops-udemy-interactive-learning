#!/usr/bin/env python3
"""Generate Helm interactive challenge HTML files from challenge definitions."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "challenges" / "helm"

CHALLENGES = [
    {
        "file": "helm-failed-upgrade.html",
        "page_title": "Failed upgrade — payments | Helm Learning",
        "welcome_title": "Failed upgrade",
        "welcome_subtitle": 'The <strong style="color:var(--accent-gold)">payments-api</strong> release in <strong style="color:var(--accent-gold)">payments</strong> is <strong style="color:var(--accent-red)">failed</strong> after CI deployed chart <strong style="color:var(--accent-gold)">2.4.0</strong> — checkout is degraded.',
        "scenario_icon": "💥",
        "scenario_h3": "Bad Helm revision",
        "scenario_description": "A <span class='hl-green'>helm upgrade</span> partially applied then failed. Revision history shows a broken revision; pods may be mixed or unhealthy. You will use <span class='hl-green'>helm status</span>, <span class='hl-green'>helm history</span>, and <span class='hl-green'>helm rollback</span> — the Helm-native escape hatch when a chart release goes wrong.",
        "tasks": [
            "List releases and confirm <code style=\"font-family:'Fira Code',monospace;font-size:0.8rem;color:var(--accent-gold)\">helm status</code> shows failed",
            "Read revision history with <code style=\"font-family:'Fira Code',monospace;font-size:0.8rem;color:var(--accent-gold)\">helm history</code>",
            "Correlate cluster symptoms with <code style=\"font-family:'Fira Code',monospace;font-size:0.8rem;color:var(--accent-gold)\">kubectl get pods</code>",
            "Inspect the bad revision manifest and roll back safely",
        ],
        "logo_label": "Failed upgrade",
        "badge": "RELEASE FAILED",
        "banner": "FAILED UPGRADE — payments-api namespace payments",
        "banner_warn": "⚠ Helm release failed — check revision history and rollback",
        "context": "Context: prod — namespace: payments — release: payments-api",
        "mission_title": "Release recovered",
        "mission_subtitle": "You read <span class='hl-green'>helm history</span>, correlated pod failures with revision <span class='hl-red'>14</span>, and used <span class='hl-green'>helm rollback</span> to restore a deployed release.<br>Follow-up: fix the chart values or image tag in CI before re-upgrading.",
        "learned_commands": [
            {"cmd": "helm list -n payments", "step": "Step 1", "desc": "See release name, revision, and status at a glance"},
            {"cmd": "helm status payments-api -n payments", "step": "Step 2", "desc": "Read NOTES, resources, and failed state detail"},
            {"cmd": "helm history payments-api -n payments", "step": "Step 3", "desc": "Revision numbers tied to deploy events"},
            {"cmd": "kubectl get pods -n payments -l app.kubernetes.io/instance=payments-api", "step": "Step 4", "desc": "Correlate release failure with pod symptoms"},
            {"cmd": "kubectl describe pod payments-api-... -n payments", "step": "Step 5", "desc": "Image pull or crash detail from Events"},
            {"cmd": "helm get manifest payments-api -n payments --revision 14", "step": "Step 6", "desc": "See what the failed revision tried to apply"},
            {"cmd": "helm get manifest payments-api -n payments --revision 13", "step": "Step 7", "desc": "Compare last known-good revision manifest"},
            {"cmd": "helm rollback payments-api 13 -n payments", "step": "Step 8", "desc": "Restore release to revision 13"},
            {"cmd": "helm status payments-api -n payments", "step": "Step 9", "desc": "Confirm status returns to deployed"},
            {"cmd": "kubectl get pods -n payments -l app.kubernetes.io/instance=payments-api", "step": "Step 10", "desc": "Verify healthy pods after rollback"},
        ],
        "steps": [
            {"id": 1, "hint": "helm list -n payments", "allowedCommands": ["helm list -n payments"],
             "simulatedOutput": [
                 {"type": "header", "text": "NAME          NAMESPACE  REVISION  UPDATED                  STATUS   CHART"},
                 {"type": "key-box-red", "text": "payments-api  payments   14        2026-06-27 08:12:04 UTC  failed   payments-api-2.4.0"},
                 {"type": "data", "text": "redis-cache   payments   3         2026-05-01 10:00:00 UTC  deployed redis-18.0.0"},
             ],
             "before": "Start with <span class='hl-green'>helm list</span> — the STATUS column shows <span class='hl-red'>failed</span> on revision 14.",
             "after": "Release <span class='hl-yellow'>payments-api</span> failed on the latest upgrade. I need <span class='hl-green'>helm status</span> for detail on what Helm recorded."},
            {"id": 2, "hint": "helm status payments-api -n payments", "allowedCommands": ["helm status payments-api -n payments"],
             "simulatedOutput": [
                 {"type": "header", "text": "NAME: payments-api"},
                 {"type": "key-box-red", "text": "STATUS: failed"},
                 {"type": "data", "text": "LAST DEPLOYED: Fri Jun 27 08:12:04 2026"},
                 {"type": "data", "text": "NAMESPACE: payments"},
                 {"type": "key-box-red", "text": "REVISION: 14"},
                 {"type": "data", "text": "DESCRIPTION: Upgrade \"payments-api\" failed: timed out waiting for condition"},
             ],
             "before": "<span class='hl-green'>helm status</span> shows revision, last deploy time, and the failure description Helm stored.",
             "after": "Revision 14 timed out — likely bad pods never became ready. I'll pull <span class='hl-green'>helm history</span> to see prior good revisions."},
            {"id": 3, "hint": "helm history payments-api -n payments", "allowedCommands": ["helm history payments-api -n payments"],
             "simulatedOutput": [
                 {"type": "header", "text": "REVISION  UPDATED                  STATUS      CHART               DESCRIPTION"},
                 {"type": "data", "text": "12        Mon Jun 10 09:00:00 2026 superseded  payments-api-2.3.1  Upgrade complete"},
                 {"type": "key-box-green", "text": "13        Mon Jun 24 14:22:00 2026 deployed    payments-api-2.3.2  Upgrade complete"},
                 {"type": "key-box-red", "text": "14        Fri Jun 27 08:12:04 2026 failed      payments-api-2.4.0  Upgrade \"payments-api\" failed"},
             ],
             "before": "<span class='hl-green'>helm history</span> lists every revision — revision <span class='hl-green'>13</span> was the last successful deploy.",
             "after": "Rollback target is revision <span class='hl-green'>13</span>. First I'll confirm pod symptoms in the cluster."},
            {"id": 4, "hint": "kubectl get pods -n payments -l app.kubernetes.io/instance=payments-api", "allowedCommands": ["kubectl get pods -n payments -l app.kubernetes.io/instance=payments-api"],
             "simulatedOutput": [
                 {"type": "header", "text": "NAME                            READY   STATUS             RESTARTS   AGE"},
                 {"type": "data", "text": "payments-api-6f8b9c7d4-aa11   1/1     Running            0          3d"},
                 {"type": "data", "text": "payments-api-6f8b9c7d4-bb22   1/1     Running            0          3d"},
                 {"type": "key-box-red", "text": "payments-api-9d2e1f0a8-cc33    0/1     ImagePullBackOff   0          12m"},
             ],
             "before": "Pods from the failed revision often show <span class='hl-red'>ImagePullBackOff</span> or <span class='hl-red'>CrashLoopBackOff</span> while old pods still run.",
             "after": "New revision pod can't pull image — classic failed upgrade symptom. I'll describe it for the exact error."},
            {"id": 5, "hint": "kubectl describe pod payments-api-9d2e1f0a8-cc33 -n payments", "allowedCommands": ["kubectl describe pod payments-api-9d2e1f0a8-cc33 -n payments"],
             "simulatedOutput": [
                 {"type": "data", "text": "Containers:"},
                 {"type": "key-box-red", "text": "  Image: registry.example.com/payments/api:v4.0.0-badtag"},
                 {"type": "data", "text": "Events:"},
                 {"type": "key-box-red", "text": "  Failed to pull image \"...v4.0.0-badtag\": not found"},
             ],
             "before": "<span class='hl-green'>kubectl describe pod</span> shows the bad image tag CI pushed in chart 2.4.0.",
             "after": "Chart 2.4.0 references a non-existent image tag. I'll inspect revision 14's manifest before rolling back."},
            {"id": 6, "hint": "helm get manifest payments-api -n payments --revision 14", "allowedCommands": ["helm get manifest payments-api -n payments --revision 14"],
             "simulatedOutput": [
                 {"type": "data", "text": "apiVersion: apps/v1"},
                 {"type": "data", "text": "kind: Deployment"},
                 {"type": "key-box-red", "text": "  image: registry.example.com/payments/api:v4.0.0-badtag"},
             ],
             "before": "<span class='hl-green'>helm get manifest --revision</span> shows exactly what Helm tried to apply for the failed release.",
             "after": "Confirmed — revision 14 manifest has the bad tag. I'll peek at revision 13 for the good image."},
            {"id": 7, "hint": "helm get manifest payments-api -n payments --revision 13", "allowedCommands": ["helm get manifest payments-api -n payments --revision 13"],
             "simulatedOutput": [
                 {"type": "data", "text": "apiVersion: apps/v1"},
                 {"type": "data", "text": "kind: Deployment"},
                 {"type": "key-box-green", "text": "  image: registry.example.com/payments/api:v3.9.2"},
             ],
             "before": "Compare the last <span class='hl-green'>deployed</span> revision manifest to confirm rollback will restore a known-good image.",
             "after": "Revision 13 uses <span class='hl-green'>v3.9.2</span> — safe rollback target. Running <span class='hl-green'>helm rollback</span>."},
            {"id": 8, "hint": "helm rollback payments-api 13 -n payments", "allowedCommands": ["helm rollback payments-api 13 -n payments"],
             "simulatedOutput": [
                 {"type": "success", "text": "Rollback was a success! Happy Helming!"},
                 {"type": "key-box-green", "text": "Release \"payments-api\" has been rolled back to revision 13."},
             ],
             "before": "<span class='hl-green'>helm rollback RELEASE REVISION</span> re-applies the manifest from that revision and creates a new history entry.",
             "after": "Rollback submitted. I'll confirm Helm status is <span class='hl-green'>deployed</span> again."},
            {"id": 9, "hint": "helm status payments-api -n payments", "allowedCommands": ["helm status payments-api -n payments"],
             "simulatedOutput": [
                 {"type": "key-box-green", "text": "STATUS: deployed"},
                 {"type": "data", "text": "REVISION: 15"},
                 {"type": "data", "text": "DESCRIPTION: Rollback to 13"},
             ],
             "before": "After rollback, status should be <span class='hl-green'>deployed</span> — note revision increments (now 15) even though config matches 13.",
             "after": "Release is healthy at the Helm layer. Final check: pods are all Running."},
            {"id": 10, "hint": "kubectl get pods -n payments -l app.kubernetes.io/instance=payments-api", "allowedCommands": ["kubectl get pods -n payments -l app.kubernetes.io/instance=payments-api"],
             "simulatedOutput": [
                 {"type": "header", "text": "NAME                            READY   STATUS    RESTARTS   AGE"},
                 {"type": "key-box-green", "text": "payments-api-6f8b9c7d4-aa11   1/1     Running   0          3d"},
                 {"type": "key-box-green", "text": "payments-api-6f8b9c7d4-bb22   1/1     Running   0          3d"},
                 {"type": "key-box-green", "text": "payments-api-6f8b9c7d4-dd44   1/1     Running   0          18s"},
             ],
             "before": "All pods should be <span class='hl-green'>Running</span> on the restored ReplicaSet — bad revision pods scaled away.",
             "after": "🎉 <span class='hl-green'>Incident contained.</span> You used <span class='hl-green'>helm history</span> and <span class='hl-green'>helm rollback</span> to restore checkout. Fix the image tag in chart 2.4.0 before re-upgrading."},
        ],
    },
    {
        "file": "helm-wrong-values.html",
        "page_title": "Wrong values — inventory | Helm Learning",
        "welcome_title": "Wrong values",
        "welcome_subtitle": '<strong style="color:var(--accent-gold)">inventory-api</strong> in <strong style="color:var(--accent-gold)">prod</strong> is up but serving staging config — someone ran upgrade with the wrong <code style="font-family:\'Fira Code\',monospace;font-size:0.85rem;color:var(--accent-gold)">-f</code> file.',
        "scenario_icon": "📋",
        "scenario_h3": "Values file mix-up",
        "scenario_description": "The release is <span class='hl-green'>deployed</span> and pods are running, but behavior is wrong. The bug is in <span class='hl-yellow'>what Helm computed from values</span> — not a crashed pod. You will trace <span class='hl-green'>helm get values</span> into rendered manifests.",
        "tasks": [
            "Read user-supplied values with <code style=\"font-family:'Fira Code',monospace;font-size:0.8rem;color:var(--accent-gold)\">helm get values</code>",
            "Compare computed values with <code style=\"font-family:'Fira Code',monospace;font-size:0.8rem;color:var(--accent-gold)\">--all</code>",
            "Trace env vars from <code style=\"font-family:'Fira Code',monospace;font-size:0.8rem;color:var(--accent-gold)\">helm get manifest</code> into the cluster",
            "Confirm the environment mismatch before re-upgrading with correct values",
        ],
        "logo_label": "Wrong values",
        "badge": "VALUES MISMATCH",
        "banner": "WRONG VALUES — inventory-api namespace prod",
        "banner_warn": "⚠ Release deployed but serving wrong environment config",
        "context": "Context: prod — namespace: prod — release: inventory-api",
        "mission_title": "Values traced",
        "mission_subtitle": "You traced <span class='hl-green'>helm get values</span> to a staging API URL baked into the prod release.<br>Follow-up: enforce values file checks in CI and separate <span class='hl-yellow'>values-prod.yaml</span> from staging.",
        "learned_commands": [
            {"cmd": "helm list -n prod", "step": "Step 1", "desc": "Confirm release shows deployed status"},
            {"cmd": "helm status inventory-api -n prod", "step": "Step 2", "desc": "Baseline release metadata"},
            {"cmd": "helm get values inventory-api -n prod", "step": "Step 3", "desc": "User-supplied values Helm stored"},
            {"cmd": "helm get values inventory-api -n prod --all", "step": "Step 4", "desc": "Computed values including chart defaults"},
            {"cmd": "helm get manifest inventory-api -n prod | grep -A3 API_URL", "step": "Step 5", "desc": "See rendered env in manifest"},
            {"cmd": "kubectl get deployment inventory-api -n prod -o yaml | grep API_URL", "step": "Step 6", "desc": "Confirm live cluster matches manifest"},
            {"cmd": "kubectl logs -n prod deploy/inventory-api --tail=20", "step": "Step 7", "desc": "App logs showing wrong upstream"},
            {"cmd": "helm history inventory-api -n prod", "step": "Step 8", "desc": "Find which upgrade introduced bad values"},
            {"cmd": "helm get values inventory-api -n prod --revision 21", "step": "Step 9", "desc": "Compare prior revision values"},
            {"cmd": "helm get values inventory-api -n prod --revision 22", "step": "Step 10", "desc": "Confirm staging values landed on revision 22"},
        ],
        "steps": [
            {"id": 1, "hint": "helm list -n prod", "allowedCommands": ["helm list -n prod"],
             "simulatedOutput": [{"type": "header", "text": "NAME            NAMESPACE  REVISION  STATUS    CHART"},
                 {"type": "key-box", "text": "inventory-api   prod       22        deployed  inventory-api-1.8.0"}],
             "before": "Pods may be green while config is wrong — <span class='hl-green'>helm list</span> still shows <span class='hl-green'>deployed</span>.",
             "after": "Release looks healthy at the Helm layer. I need to inspect what values were applied."},
            {"id": 2, "hint": "helm status inventory-api -n prod", "allowedCommands": ["helm status inventory-api -n prod"],
             "simulatedOutput": [{"type": "key-box-green", "text": "STATUS: deployed"}, {"type": "data", "text": "REVISION: 22"}, {"type": "data", "text": "CHART: inventory-api-1.8.0"}],
             "before": "<span class='hl-green'>helm status</span> confirms we're debugging revision 22 — the latest upgrade.",
             "after": "Revision 22 is live. I'll read the user-supplied values Helm stored for this release."},
            {"id": 3, "hint": "helm get values inventory-api -n prod", "allowedCommands": ["helm get values inventory-api -n prod"],
             "simulatedOutput": [{"type": "data", "text": "env:"}, {"type": "key-box-red", "text": "  API_URL: https://staging-api.example.com"}, {"type": "data", "text": "replicaCount: 3"}, {"type": "key-box-red", "text": "  LOG_LEVEL: debug"}],
             "before": "<span class='hl-green'>helm get values</span> shows only user-supplied overrides — not chart defaults.",
             "after": "<span class='hl-red'>staging-api.example.com</span> in prod! That's the smoking gun. I'll check computed values with <span class='hl-yellow'>--all</span>."},
            {"id": 4, "hint": "helm get values inventory-api -n prod --all", "allowedCommands": ["helm get values inventory-api -n prod --all"],
             "simulatedOutput": [{"type": "data", "text": "COMPUTED VALUES:"}, {"type": "key-box-red", "text": "  env.API_URL: https://staging-api.example.com"}, {"type": "data", "text": "  image.repository: registry.example.com/inventory/api"}, {"type": "data", "text": "  image.tag: 1.8.0"}],
             "before": "<span class='hl-green'>--all</span> merges chart defaults with overrides — confirms staging URL is what Helm rendered.",
             "after": "Values layer is wrong, not the chart templates. I'll verify the manifest actually contains this env var."},
            {"id": 5, "hint": "helm get manifest inventory-api -n prod | grep -A3 API_URL", "allowedCommands": ["helm get manifest inventory-api -n prod | grep -A3 API_URL"],
             "simulatedOutput": [{"type": "key-box-red", "text": "        - name: API_URL"}, {"type": "key-box-red", "text": "          value: https://staging-api.example.com"}],
             "before": "<span class='hl-green'>helm get manifest</span> pipes rendered YAML — grep for the env var you suspect.",
             "after": "Manifest confirms staging URL is baked in. Does the live Deployment match?"}, 
            {"id": 6, "hint": "kubectl get deployment inventory-api -n prod -o yaml | grep API_URL", "allowedCommands": ["kubectl get deployment inventory-api -n prod -o yaml | grep API_URL"],
             "simulatedOutput": [{"type": "key-box-red", "text": "        - name: API_URL"}, {"type": "key-box-red", "text": "          value: https://staging-api.example.com"}],
             "before": "Compare Helm manifest to live object — they should match if nothing was manually edited.",
             "after": "Cluster matches Helm manifest — pure values mistake. App logs should show calls to staging."},
            {"id": 7, "hint": "kubectl logs -n prod deploy/inventory-api --tail=20", "allowedCommands": ["kubectl logs -n prod deploy/inventory-api --tail=20"],
             "simulatedOutput": [{"type": "warning", "text": "WARN upstream=staging-api.example.com latency=890ms route=/sync"}, {"type": "key-box-red", "text": "ERROR staging catalog returned test SKUs to prod traffic"}],
             "before": "Application logs often prove the misconfiguration faster than YAML alone.",
             "after": "Prod traffic hitting staging upstream. I need to know when this values file was applied."},
            {"id": 8, "hint": "helm history inventory-api -n prod", "allowedCommands": ["helm history inventory-api -n prod"],
             "simulatedOutput": [{"type": "header", "text": "REVISION  STATUS      DESCRIPTION"}, {"type": "key-box-green", "text": "21        superseded  Upgrade complete"}, {"type": "key-box-red", "text": "22        deployed    Upgrade complete — pipeline used values-staging.yaml"}],
             "before": "<span class='hl-green'>helm history</span> DESCRIPTION field often records CI context — who deployed what.",
             "after": "Revision 22 introduced the bad values. I'll compare revision 21's values."},
            {"id": 9, "hint": "helm get values inventory-api -n prod --revision 21", "allowedCommands": ["helm get values inventory-api -n prod --revision 21"],
             "simulatedOutput": [{"type": "key-box-green", "text": "  API_URL: https://api.example.com"}, {"type": "data", "text": "  LOG_LEVEL: info"}],
             "before": "<span class='hl-green'>helm get values --revision N</span> shows values from any prior release.",
             "after": "Revision 21 had the correct prod URL. Revision 22 is definitely the bad deploy."},
            {"id": 10, "hint": "helm get values inventory-api -n prod --revision 22", "allowedCommands": ["helm get values inventory-api -n prod --revision 22"],
             "simulatedOutput": [{"type": "key-box-red", "text": "  API_URL: https://staging-api.example.com"}, {"type": "key-box-red", "text": "  LOG_LEVEL: debug"}],
             "before": "Confirm revision 22 values match what you found on the current release.",
             "after": "🎉 <span class='hl-green'>Root cause confirmed.</span> Wrong <span class='hl-yellow'>-f values-staging.yaml</span> on prod upgrade. Fix: rollback or re-upgrade with <span class='hl-green'>values-prod.yaml</span>."},
        ],
    },
    {
        "file": "helm-hook-failed.html",
        "page_title": "Hook failed — orders-db | Helm Learning",
        "welcome_title": "Hook failed",
        "welcome_subtitle": '<strong style="color:var(--accent-gold)">orders-db</strong> upgrade in <strong style="color:var(--accent-gold)">orders</strong> is stuck <strong style="color:var(--accent-yellow)">pending-upgrade</strong> — the migration hook never finished.',
        "scenario_icon": "🪝",
        "scenario_h3": "Blocked by hook",
        "scenario_description": "A <span class='hl-yellow'>post-upgrade</span> Helm hook Job is failing. The release cannot complete until the hook succeeds. You will use <span class='hl-green'>helm status</span>, <span class='hl-green'>helm get hooks</span>, and hook Job logs.",
        "tasks": [
            "Confirm <code style=\"font-family:'Fira Code',monospace;font-size:0.8rem;color:var(--accent-gold)\">pending-upgrade</code> with helm status",
            "List hook resources via <code style=\"font-family:'Fira Code',monospace;font-size:0.8rem;color:var(--accent-gold)\">helm get hooks</code>",
            "Find failing hook Jobs with kubectl labels",
            "Read hook Job logs and decide rollback vs fix-forward",
        ],
        "logo_label": "Hook failed",
        "badge": "HOOK BLOCKED",
        "banner": "HOOK FAILED — orders-db namespace orders",
        "banner_warn": "⚠ Helm upgrade pending — post-upgrade hook Job failing",
        "context": "Context: prod — namespace: orders — release: orders-db",
        "mission_title": "Hook diagnosed",
        "mission_subtitle": "You traced a <span class='hl-yellow'>pending-upgrade</span> to a failing <span class='hl-green'>post-upgrade</span> migration hook and read the SQL error from hook logs.<br>Follow-up: fix migration script, test hooks in staging, add hook timeout alerts.",
        "learned_commands": [
            {"cmd": "helm list -n orders", "step": "Step 1", "desc": "See pending-upgrade status"},
            {"cmd": "helm status orders-db -n orders", "step": "Step 2", "desc": "Read pending state description"},
            {"cmd": "helm get hooks orders-db -n orders", "step": "Step 3", "desc": "List hook manifests Helm created"},
            {"cmd": "kubectl get jobs -n orders -l helm.sh/hook", "step": "Step 4", "desc": "Find hook Jobs in the namespace"},
            {"cmd": "kubectl describe job orders-db-migrate-14 -n orders", "step": "Step 5", "desc": "Hook Job events and failure reason"},
            {"cmd": "kubectl get pods -n orders -l job-name=orders-db-migrate-14", "step": "Step 6", "desc": "Locate hook pod for log access"},
            {"cmd": "kubectl logs -n orders orders-db-migrate-14-abc12", "step": "Step 7", "desc": "Migration error from hook container"},
            {"cmd": "helm history orders-db -n orders", "step": "Step 8", "desc": "See which revision triggered the hook"},
            {"cmd": "kubectl get events -n orders --sort-by=.lastTimestamp", "step": "Step 9", "desc": "Hook lifecycle events"},
            {"cmd": "helm rollback orders-db 13 -n orders", "step": "Step 10", "desc": "Restore service while migration is fixed"},
        ],
        "steps": [
            {"id": 1, "hint": "helm list -n orders", "allowedCommands": ["helm list -n orders"],
             "simulatedOutput": [{"type": "key-box-red", "text": "orders-db  orders  14  pending-upgrade  orders-db-3.2.0"}],
             "before": "<span class='hl-red'>pending-upgrade</span> means Helm started an upgrade but hasn't marked it complete — often a hook is blocking.",
             "after": "Release stuck mid-upgrade. <span class='hl-green'>helm status</span> should explain what's pending."},
            {"id": 2, "hint": "helm status orders-db -n orders", "allowedCommands": ["helm status orders-db -n orders"],
             "simulatedOutput": [{"type": "key-box-red", "text": "STATUS: pending-upgrade"}, {"type": "data", "text": "REVISION: 14"}, {"type": "key-box-red", "text": "DESCRIPTION: Waiting for post-upgrade hooks to complete"}],
             "before": "Status DESCRIPTION often names the hook phase blocking completion.",
             "after": "Post-upgrade hook is the blocker. I'll list hook resources Helm created."},
            {"id": 3, "hint": "helm get hooks orders-db -n orders", "allowedCommands": ["helm get hooks orders-db -n orders"],
             "simulatedOutput": [{"type": "header", "text": "HOOK MANIFEST (post-upgrade):"}, {"type": "data", "text": "kind: Job"}, {"type": "key-box", "text": "  name: orders-db-migrate-14"}, {"type": "data", "text": "  annotations: helm.sh/hook: post-upgrade"}],
             "before": "<span class='hl-green'>helm get hooks</span> shows hook manifests — note the Job name and hook annotation.",
             "after": "Hook Job is <span class='hl-yellow'>orders-db-migrate-14</span>. I'll find it in the cluster with hook labels."},
            {"id": 4, "hint": "kubectl get jobs -n orders -l helm.sh/hook", "allowedCommands": ["kubectl get jobs -n orders -l helm.sh/hook"],
             "simulatedOutput": [{"type": "header", "text": "NAME                    COMPLETIONS   DURATION   AGE"}, {"type": "key-box-red", "text": "orders-db-migrate-14    0/1           8m         8m"}],
             "before": "Hook Jobs carry <span class='hl-yellow'>helm.sh/hook</span> labels — filter with <span class='hl-green'>-l</span>.",
             "after": "Job never completed (0/1). I'll describe it for Events."},
            {"id": 5, "hint": "kubectl describe job orders-db-migrate-14 -n orders", "allowedCommands": ["kubectl describe job orders-db-migrate-14 -n orders"],
             "simulatedOutput": [{"type": "data", "text": "Pods Statuses:  0 Running / 1 Failed"}, {"type": "key-box-red", "text": "  Warning  BackoffLimitExceeded  job has reached the specified backoff limit"}],
             "before": "<span class='hl-green'>describe job</span> shows backoff exhaustion when hook retries are spent.",
             "after": "Hook pod failed repeatedly. I need the pod name to read logs."},
            {"id": 6, "hint": "kubectl get pods -n orders -l job-name=orders-db-migrate-14", "allowedCommands": ["kubectl get pods -n orders -l job-name=orders-db-migrate-14"],
             "simulatedOutput": [{"type": "key-box-red", "text": "orders-db-migrate-14-abc12   0/1   Error   0   8m"}],
             "before": "Hook pods are named after the Job — filter with <span class='hl-yellow'>job-name=</span> label.",
             "after": "Pod exited with Error. Pulling migration logs."},
            {"id": 7, "hint": "kubectl logs -n orders orders-db-migrate-14-abc12", "allowedCommands": ["kubectl logs -n orders orders-db-migrate-14-abc12"],
             "simulatedOutput": [{"type": "data", "text": "Running migration 20260627_add_orders_index.sql..."}, {"type": "key-box-red", "text": "ERROR: relation \"orders_archive\" already exists"}, {"type": "error", "text": "migration failed: exit status 1"}],
             "before": "Hook container logs reveal the migration SQL error — the real root cause.",
             "after": "Migration tries to create a table that already exists — non-idempotent script. Check which revision triggered this."},
            {"id": 8, "hint": "helm history orders-db -n orders", "allowedCommands": ["helm history orders-db -n orders"],
             "simulatedOutput": [{"type": "key-box-green", "text": "13  deployed    orders-db-3.1.0  Upgrade complete"}, {"type": "key-box-red", "text": "14  pending-upgrade  orders-db-3.2.0  Preparing upgrade"}],
             "before": "<span class='hl-green'>helm history</span> shows revision 14 never reached deployed because the hook failed.",
             "after": "Revision 14 is stuck. I'll skim events for the hook timeline."},
            {"id": 9, "hint": "kubectl get events -n orders --sort-by=.lastTimestamp", "allowedCommands": ["kubectl get events -n orders --sort-by=.lastTimestamp"],
             "simulatedOutput": [{"type": "data", "text": "8m   Normal   Created   job/orders-db-migrate-14"}, {"type": "key-box-red", "text": "2m   Warning  BackoffLimitExceeded  job/orders-db-migrate-14"}],
             "before": "Events confirm hook Job creation and eventual backoff failure.",
             "after": "While the migration is fixed, rollback to revision 13 restores a deployed release."},
            {"id": 10, "hint": "helm rollback orders-db 13 -n orders", "allowedCommands": ["helm rollback orders-db 13 -n orders"],
             "simulatedOutput": [{"type": "success", "text": "Rollback was a success! Happy Helming!"}, {"type": "key-box-green", "text": "Release \"orders-db\" has been rolled back to revision 13."}],
             "before": "<span class='hl-green'>helm rollback</span> clears pending-upgrade and restores the last good revision while you fix the hook script.",
             "after": "🎉 <span class='hl-green'>Upgrade unblocked.</span> You diagnosed a failing <span class='hl-yellow'>post-upgrade</span> hook via labels and logs. Fix the idempotent migration before re-upgrading to 3.2.0."},
        ],
    },
    {
        "file": "helm-template-bug.html",
        "page_title": "Template bug — notifications | Helm Learning",
        "welcome_title": "Template bug",
        "welcome_subtitle": '<strong style="color:var(--accent-gold)">notifications-worker</strong> in <strong style="color:var(--accent-gold)">platform</strong> was upgraded with a new image tag in values, but pods still run the old image.',
        "scenario_icon": "📝",
        "scenario_h3": "Template path typo",
        "scenario_description": "Values look correct at the Helm layer, but the chart template references the wrong values path. The rendered Deployment never picks up the new image tag. You will compare <span class='hl-green'>helm get values</span> to <span class='hl-green'>helm get manifest</span> and live objects.",
        "tasks": [
            "Confirm new tag in <code style=\"font-family:'Fira Code',monospace;font-size:0.8rem;color:var(--accent-gold)\">helm get values</code>",
            "Compare rendered image in <code style=\"font-family:'Fira Code',monospace;font-size:0.8rem;color:var(--accent-gold)\">helm get manifest</code>",
            "Verify live Deployment image with kubectl",
            "Render locally with <code style=\"font-family:'Fira Code',monospace;font-size:0.8rem;color:var(--accent-gold)\">helm template</code> to spot the template path bug",
        ],
        "logo_label": "Template bug",
        "badge": "TEMPLATE DRIFT",
        "banner": "TEMPLATE BUG — notifications-worker namespace platform",
        "banner_warn": "⚠ Values updated but Deployment image unchanged",
        "context": "Context: prod — namespace: platform — release: notifications-worker",
        "mission_title": "Template bug found",
        "mission_subtitle": "You proved values had <span class='hl-green'>worker.image.tag: v2.4.0</span> but the template read <span class='hl-red'>.Values.image.tag</span> — so the old image persisted.<br>Follow-up: fix the template path and add a chart test that asserts rendered image matches values.",
        "learned_commands": [
            {"cmd": "helm list -n platform", "step": "Step 1", "desc": "Confirm deployed release revision"},
            {"cmd": "helm get values notifications-worker -n platform", "step": "Step 2", "desc": "See worker.image.tag in values"},
            {"cmd": "helm get manifest notifications-worker -n platform | grep image:", "step": "Step 3", "desc": "Rendered image in Helm manifest"},
            {"cmd": "kubectl get deployment notifications-worker -n platform", "step": "Step 4", "desc": "Quick check deployment exists"},
            {"cmd": "kubectl get deployment notifications-worker -n platform -o jsonpath='{.spec.template.spec.containers[0].image}'", "step": "Step 5", "desc": "Live image on cluster"},
            {"cmd": "kubectl get pods -n platform -l app.kubernetes.io/instance=notifications-worker", "step": "Step 6", "desc": "Pods still on old image"},
            {"cmd": "helm history notifications-worker -n platform", "step": "Step 7", "desc": "Upgrade did run — revision incremented"},
            {"cmd": "helm get manifest notifications-worker -n platform --revision 18", "step": "Step 8", "desc": "Prior revision image for comparison"},
            {"cmd": "helm template notifications-worker ./chart -f values.yaml | grep image:", "step": "Step 9", "desc": "Local render exposes template path bug"},
            {"cmd": "helm get values notifications-worker -n platform --all", "step": "Step 10", "desc": "Confirm nested worker.image structure in values"},
        ],
        "steps": [
            {"id": 1, "hint": "helm list -n platform", "allowedCommands": ["helm list -n platform"],
             "simulatedOutput": [{"type": "key-box", "text": "notifications-worker  platform  19  deployed  notifications-2.4.0"}],
             "before": "Release shows <span class='hl-green'>deployed</span> — Helm thinks the upgrade succeeded.",
             "after": "Revision 19 deployed. But users report old worker behavior — check values first."},
            {"id": 2, "hint": "helm get values notifications-worker -n platform", "allowedCommands": ["helm get values notifications-worker -n platform"],
             "simulatedOutput": [{"type": "data", "text": "worker:"}, {"type": "key-box-green", "text": "  image:"}, {"type": "key-box-green", "text": "    tag: v2.4.0"}, {"type": "data", "text": "image:"}, {"type": "data", "text": "  tag: v2.3.1"}],
             "before": "Values show <span class='hl-green'>worker.image.tag: v2.4.0</span> — the tag CI intended to deploy.",
             "after": "Values are correct at the nested path. Does the manifest use them?"}, 
            {"id": 3, "hint": "helm get manifest notifications-worker -n platform | grep image:", "allowedCommands": ["helm get manifest notifications-worker -n platform | grep image:"],
             "simulatedOutput": [{"type": "key-box-red", "text": "        image: registry.example.com/notifications/worker:v2.3.1"}],
             "before": "<span class='hl-green'>helm get manifest | grep image</span> shows what Helm actually rendered.",
             "after": "<span class='hl-red'>v2.3.1</span> in manifest despite values saying v2.4.0 — template isn't reading the right path."},
            {"id": 4, "hint": "kubectl get deployment notifications-worker -n platform", "allowedCommands": ["kubectl get deployment notifications-worker -n platform"],
             "simulatedOutput": [{"type": "key-box", "text": "notifications-worker   3/3   3   3   45d"}],
             "before": "Deployment is healthy — three of three ready — masking the stale image.",
             "after": "All replicas ready but wrong version. Pull the exact image string from the live spec."},
            {"id": 5, "hint": "kubectl get deployment notifications-worker -n platform -o jsonpath='{.spec.template.spec.containers[0].image}'", "allowedCommands": ["kubectl get deployment notifications-worker -n platform -o jsonpath='{.spec.template.spec.containers[0].image}'"],
             "simulatedOutput": [{"type": "key-box-red", "text": "registry.example.com/notifications/worker:v2.3.1"}],
             "before": "<span class='hl-green'>jsonpath</span> extracts the image field without dumping full YAML.",
             "after": "Cluster matches manifest — both stuck on v2.3.1. Check if pods inherited it."},
            {"id": 6, "hint": "kubectl get pods -n platform -l app.kubernetes.io/instance=notifications-worker", "allowedCommands": ["kubectl get pods -n platform -l app.kubernetes.io/instance=notifications-worker"],
             "simulatedOutput": [{"type": "data", "text": "notifications-worker-7a1b2c3d4-aa11   1/1   Running   0   2h"}, {"type": "data", "text": "notifications-worker-7a1b2c3d4-bb22   1/1   Running   0   2h"}],
             "before": "Pods may have been recreated during upgrade but still pull the wrong image from the Deployment spec.",
             "after": "Pods are young (2h) — upgrade did roll pods, just with wrong image in template."},
            {"id": 7, "hint": "helm history notifications-worker -n platform", "allowedCommands": ["helm history notifications-worker -n platform"],
             "simulatedOutput": [{"type": "data", "text": "18  superseded  notifications-2.3.1"}, {"type": "key-box", "text": "19  deployed    notifications-2.4.0  Upgrade complete"}],
             "before": "History proves Helm ran the upgrade — this isn't a 'forgot to deploy' problem.",
             "after": "Revision 19 deployed but image unchanged. Compare revision 18 manifest."},
            {"id": 8, "hint": "helm get manifest notifications-worker -n platform --revision 18", "allowedCommands": ["helm get manifest notifications-worker -n platform --revision 18"],
             "simulatedOutput": [{"type": "key-box", "text": "        image: registry.example.com/notifications/worker:v2.3.1"}],
             "before": "If revision 18 and 19 manifests have the same image, the template bug predates this values change.",
             "after": "Same image in rev 18 and 19 — template never consumed <span class='hl-yellow'>worker.image.tag</span>. Local render next."},
            {"id": 9, "hint": "helm template notifications-worker ./chart -f values.yaml | grep image:", "allowedCommands": ["helm template notifications-worker ./chart -f values.yaml | grep image:"],
             "simulatedOutput": [{"type": "warning", "text": "# templates/deployment.yaml uses: {{ .Values.image.tag }}"}, {"type": "key-box-red", "text": "        image: registry.example.com/notifications/worker:v2.3.1"}],
             "before": "<span class='hl-green'>helm template</span> renders locally — ideal for spotting template path typos before prod.",
             "after": "Template reads <span class='hl-red'>.Values.image.tag</span> (v2.3.1) instead of <span class='hl-green'>.Values.worker.image.tag</span> (v2.4.0)."}, 
            {"id": 10, "hint": "helm get values notifications-worker -n platform --all", "allowedCommands": ["helm get values notifications-worker -n platform --all"],
             "simulatedOutput": [{"type": "key-box-green", "text": "worker.image.tag: v2.4.0"}, {"type": "data", "text": "image.tag: v2.3.1  (chart default, wrong path)"}],
             "before": "<span class='hl-green'>--all</span> shows both nested worker values and the stale top-level default the template uses.",
             "after": "🎉 <span class='hl-green'>Root cause found.</span> Fix template to use <span class='hl-green'>.Values.worker.image.tag</span>, then re-upgrade. Chart tests should assert rendered image."},
        ],
    },
    {
        "file": "helm-upgrade-conflict.html",
        "page_title": "Upgrade conflict — auth-gateway | Helm Learning",
        "welcome_title": "Upgrade conflict",
        "welcome_subtitle": '<strong style="color:var(--accent-gold)">helm upgrade</strong> for <strong style="color:var(--accent-gold)">auth-gateway</strong> in <strong style="color:var(--accent-gold)">identity</strong> fails with a patch conflict — someone edited live resources by hand.',
        "scenario_icon": "⚡",
        "scenario_h3": "Manual drift",
        "scenario_description": "On-call ran <span class='hl-yellow'>kubectl scale</span> or <span class='hl-yellow'>kubectl edit</span> outside Helm. The next <span class='hl-green'>helm upgrade</span> fails because live state diverges from the last applied manifest. You will compare Helm ownership metadata to live specs.",
        "tasks": [
            "Reproduce the failed <code style=\"font-family:'Fira Code',monospace;font-size:0.8rem;color:var(--accent-gold)\">helm upgrade</code> error",
            "Read last applied manifest with <code style=\"font-family:'Fira Code',monospace;font-size:0.8rem;color:var(--accent-gold)\">helm get manifest</code>",
            "Compare live Deployment spec to what Helm expects",
            "Identify manual drift via annotations and replica count",
        ],
        "logo_label": "Upgrade conflict",
        "badge": "DRIFT DETECTED",
        "banner": "UPGRADE CONFLICT — auth-gateway namespace identity",
        "banner_warn": "⚠ helm upgrade fails — live resources diverged from release",
        "context": "Context: prod — namespace: identity — release: auth-gateway",
        "mission_title": "Drift identified",
        "mission_subtitle": "You found manual <span class='hl-yellow'>kubectl scale</span> changed replicas to 5 while Helm manifest expects 3 — causing the upgrade patch conflict.<br>Follow-up: enforce GitOps, document emergency scale procedures, use <span class='hl-green'>helm upgrade --force</span> only with care.",
        "learned_commands": [
            {"cmd": "helm status auth-gateway -n identity", "step": "Step 1", "desc": "Current release baseline"},
            {"cmd": "helm upgrade auth-gateway ./chart -n identity -f values.yaml", "step": "Step 2", "desc": "Reproduce patch conflict error"},
            {"cmd": "helm get manifest auth-gateway -n identity | grep replicas:", "step": "Step 3", "desc": "Replicas Helm expects to apply"},
            {"cmd": "kubectl get deployment auth-gateway -n identity", "step": "Step 4", "desc": "Live desired vs ready count"},
            {"cmd": "kubectl get deployment auth-gateway -n identity -o yaml | grep replicas:", "step": "Step 5", "desc": "Actual spec.replicas on cluster"},
            {"cmd": "kubectl get deployment auth-gateway -n identity -o jsonpath='{.metadata.annotations}'", "step": "Step 6", "desc": "Helm ownership annotations"},
            {"cmd": "kubectl get deployment auth-gateway -n identity --show-labels", "step": "Step 7", "desc": "app.kubernetes.io/managed-by label"},
            {"cmd": "helm history auth-gateway -n identity", "step": "Step 8", "desc": "Last successful Helm revision"},
            {"cmd": "kubectl get events -n identity --sort-by=.lastTimestamp", "step": "Step 9", "desc": "Manual scale event in audit trail"},
            {"cmd": "helm upgrade auth-gateway ./chart -n identity -f values.yaml --force", "step": "Step 10", "desc": "Reconcile drift (conceptual recovery)"},
        ],
        "steps": [
            {"id": 1, "hint": "helm status auth-gateway -n identity", "allowedCommands": ["helm status auth-gateway -n identity"],
             "simulatedOutput": [{"type": "key-box-green", "text": "STATUS: deployed"}, {"type": "data", "text": "REVISION: 11"}, {"type": "data", "text": "CHART: auth-gateway-1.5.0"}],
             "before": "Release still shows <span class='hl-green'>deployed</span> from revision 11 — but a new upgrade is failing.",
             "after": "Last successful deploy was rev 11. I'll attempt the upgrade that CI reported as failed."},
            {"id": 2, "hint": "helm upgrade auth-gateway ./chart -n identity -f values.yaml", "allowedCommands": ["helm upgrade auth-gateway ./chart -n identity -f values.yaml"],
             "simulatedOutput": [{"type": "key-box-red", "text": "Error: UPGRADE FAILED: cannot patch \"auth-gateway\" with kind Deployment:"}, {"type": "key-box-red", "text": "  Deployment.apps \"auth-gateway\" is invalid: spec.replicas: Invalid value: 3: may not decrease replicas"}],
             "before": "Reproduce the error — Helm uses three-way merge and rejects changes that conflict with live edits.",
             "after": "Patch conflict on <span class='hl-yellow'>spec.replicas</span> — someone scaled outside Helm. Check what Helm wants."},
            {"id": 3, "hint": "helm get manifest auth-gateway -n identity | grep replicas:", "allowedCommands": ["helm get manifest auth-gateway -n identity | grep replicas:"],
             "simulatedOutput": [{"type": "key-box", "text": "  replicas: 3"}],
             "before": "<span class='hl-green'>helm get manifest</span> shows replicas from the chart values — Helm expects 3.",
             "after": "Helm wants 3 replicas. What's actually on the cluster?"}, 
            {"id": 4, "hint": "kubectl get deployment auth-gateway -n identity", "allowedCommands": ["kubectl get deployment auth-gateway -n identity"],
             "simulatedOutput": [{"type": "key-box-red", "text": "auth-gateway   5/5   5   5   200d"}],
             "before": "DESIRED column shows 5 — manual scale during yesterday's traffic spike.",
             "after": "Live desired is 5, Helm expects 3 — classic drift. Pull full spec."},
            {"id": 5, "hint": "kubectl get deployment auth-gateway -n identity -o yaml | grep replicas:", "allowedCommands": ["kubectl get deployment auth-gateway -n identity -o yaml | grep replicas:"],
             "simulatedOutput": [{"type": "key-box-red", "text": "  replicas: 5"}, {"type": "data", "text": "  status:"}, {"type": "data", "text": "    replicas: 5"}],
             "before": "Confirm <span class='hl-yellow'>spec.replicas</span> in live YAML — this is what blocks the patch.",
             "after": "spec.replicas is 5. Check Helm ownership metadata — this resource is still Helm-managed."},
            {"id": 6, "hint": "kubectl get deployment auth-gateway -n identity -o jsonpath='{.metadata.annotations}'", "allowedCommands": ["kubectl get deployment auth-gateway -n identity -o jsonpath='{.metadata.annotations}'"],
             "simulatedOutput": [{"type": "key-box", "text": "meta.helm.sh/release-name: auth-gateway"}, {"type": "key-box", "text": "meta.helm.sh/release-namespace: identity"}],
             "before": "Helm annotations prove ownership — manual edits don't remove Helm's claim on the object.",
             "after": "Still Helm-owned. Labels should show managed-by too."},
            {"id": 7, "hint": "kubectl get deployment auth-gateway -n identity --show-labels", "allowedCommands": ["kubectl get deployment auth-gateway -n identity --show-labels"],
             "simulatedOutput": [{"type": "key-box", "text": "app.kubernetes.io/managed-by=Helm,app.kubernetes.io/instance=auth-gateway"}],
             "before": "<span class='hl-yellow'>managed-by=Helm</span> means the next upgrade will try to reconcile spec — and hit conflicts.",
             "after": "Fully Helm-managed but manually scaled. Check events for who scaled it."},
            {"id": 8, "hint": "helm history auth-gateway -n identity", "allowedCommands": ["helm history auth-gateway -n identity"],
             "simulatedOutput": [{"type": "key-box-green", "text": "11  deployed  auth-gateway-1.5.0  Upgrade complete"}, {"type": "data", "text": "12  failed     auth-gateway-1.5.1  Upgrade failed — patch conflict"}],
             "before": "Revision 12 failed — no changes applied. Revision 11 manifest still defines intent.",
             "after": "Failed upgrade is revision 12. Events may show the manual scale."},
            {"id": 9, "hint": "kubectl get events -n identity --sort-by=.lastTimestamp", "allowedCommands": ["kubectl get events -n identity --sort-by=.lastTimestamp"],
             "simulatedOutput": [{"type": "key-box", "text": "1h ago  Normal  ScalingReplicaSet  deployment/auth-gateway  Scaled up replica set to 5"}, {"type": "data", "text": "30m ago  Warning  UpgradeFailed  release/auth-gateway  cannot patch Deployment"}],
             "before": "Events often show the manual scale and subsequent failed upgrade in sequence.",
             "after": "Scale to 5 was manual; upgrade failed 30m later. Recovery: scale back via values or use controlled reconcile."},
            {"id": 10, "hint": "helm upgrade auth-gateway ./chart -n identity -f values.yaml --force", "allowedCommands": ["helm upgrade auth-gateway ./chart -n identity -f values.yaml --force"],
             "simulatedOutput": [{"type": "warning", "text": "WARNING: --force will re-create resources on conflict"}, {"type": "success", "text": "Release \"auth-gateway\" has been upgraded. Happy Helming!"}, {"type": "key-box-green", "text": "REVISION: 13  STATUS: deployed  replicas: 3"}],
             "before": "<span class='hl-green'>--force</span> is a last resort — recreates resources. Better: update values to match intentional scale, then upgrade normally.",
             "after": "🎉 <span class='hl-green'>Drift resolved.</span> You traced a patch conflict to manual <span class='hl-yellow'>kubectl scale</span>. Policy: no manual edits on Helm-managed resources without updating values."},
        ],
    },
]

TEMPLATE = (ROOT / "challenges" / "k8" / "k8-rollout-stuck.html").read_text()

def build_html(c):
    html = TEMPLATE
    # Global helm branding
    html = html.replace("Kubernetes Learning", "Helm Learning")
    html = html.replace("cluster-admin@prod — kubectl", "cluster-admin@prod — helm")
    html = html.replace('<span class="prompt-host">k8s</span>', '<span class="prompt-host">helm</span>')
    html = html.replace("☸️", "⛵")
    html = html.replace("kubectl", "HELM_PLACEHOLDER")  # temp protect
    html = html.replace("HELM_PLACEHOLDER", "kubectl")  # restore - only wanted prompt change

    # Fix prompt in JS PROMPT_HTML and steps - re-read and do targeted replaces
    html = html.replace(
        '<span class="prompt-user">ops</span><span class="prompt-at">@</span><span class="prompt-host">k8s</span>',
        '<span class="prompt-user">ops</span><span class="prompt-at">@</span><span class="prompt-host">helm</span>',
    )

    html = html.replace("<title>Rollout stuck — catalog | Helm Learning</title>", f"<title>{c['page_title']}</title>")
    html = html.replace("<h1 class=\"welcome-title\">Rollout stuck</h1>", f"<h1 class=\"welcome-title\">{c['welcome_title']}</h1>")
    html = html.replace(
        '<p class="welcome-subtitle">A new <strong style="color:var(--accent-gold)">catalog-api</strong> release in namespace <strong style="color:var(--accent-gold)">catalog</strong> never reaches healthy — the Deployment is mid-rollout.</p>',
        f'<p class="welcome-subtitle">{c["welcome_subtitle"]}</p>',
    )
    html = html.replace('<div class="scenario-icon">🚀</div>', f'<div class="scenario-icon">{c["scenario_icon"]}</div>')
    html = html.replace("<h3>Bad revision</h3>", f"<h3>{c['scenario_h3']}</h3>")
    html = html.replace(
        """<p class="scenario-description">
                CI pushed a broken image tag. You will use <span class="hl-green">rollout status</span>, <span class="hl-green">get rs</span>, and <span class="hl-green">rollout history</span> to see which ReplicaSet is failing, then <span class='hl-green'>rollout undo</span> to restore service — the standard production escape hatch when the new revision is bad.
            </p>""",
        f'<p class="scenario-description">\n                {c["scenario_description"]}\n            </p>',
    )
    tasks_html = "\n".join(f'                    <li class="task-item"><span class="task-bullet">▸</span> {t}</li>' for t in c["tasks"])
    html = html.replace(
        """<ul class="task-list">
                    <li class="task-item"><span class="task-bullet">▸</span> Inspect Deployment health and <code style="font-family:'Fira Code',monospace;font-size:0.8rem;color:var(--accent-gold)">rollout status</code></li>
                    <li class="task-item"><span class="task-bullet">▸</span> Compare ReplicaSets and revision numbers</li>
                    <li class="task-item"><span class="task-bullet">▸</span> Read pod failure from <code style="font-family:'Fira Code',monospace;font-size:0.8rem;color:var(--accent-gold)">describe</code> / image field</li>
                    <li class="task-item"><span class="task-bullet">▸</span> Roll back to a known-good revision</li>
                </ul>""",
        f"<ul class=\"task-list\">\n{tasks_html}\n                </ul>",
    )
    html = html.replace('<div class="logo-icon">⛵</div> Rollout stuck</div>', f'<div class="logo-icon">⛵</div> {c["logo_label"]}</div>')
    html = html.replace('<div class="incident-badge">ROLLOUT STUCK</div>', f'<div class="incident-badge">{c["badge"]}</div>')
    html = html.replace('<div class="mission-title">Rollout recovered</div>', f'<div class="mission-title">{c["mission_title"]}</div>')
    html = html.replace(
        """<div class="mission-subtitle">
            You identified a bad image revision, used <span class="hl-green">rollout history</span> and <span class="hl-green">rollout undo</span>, and verified pods return to <span class="hl-green">Running</span>.<br>
            Follow-up: fix CI image tags, add canary or progressive delivery, and block `:latest` in prod.
        </div>""",
        f'<div class="mission-subtitle">\n            {c["mission_subtitle"]}\n        </div>',
    )

    # Replace steps and learnedCommands via script section
    import re
    steps_js = json.dumps(c["steps"], indent=4)
    learned_js = json.dumps(c["learned_commands"], indent=4)

    def replace_const_block(text, name, new_json):
        marker = f"const {name} = "
        start = text.index(marker) + len(marker)
        if text[start] != "[":
            raise ValueError(f"Expected array after {name}")
        depth = 0
        i = start
        while i < len(text):
            ch = text[i]
            if ch == "[":
                depth += 1
            elif ch == "]":
                depth -= 1
                if depth == 0:
                    end = i + 1
                    if text[end:end + 1] == ";":
                        end += 1
                    return text[:start] + new_json + text[end:]
            i += 1
        raise ValueError(f"Unclosed array for {name}")

    html = replace_const_block(html, "steps", steps_js)
    html = replace_const_block(html, "learnedCommands", learned_js)

    html = html.replace("ROLLOUT stuck — catalog-api namespace catalog", c["banner"])
    html = html.replace("⚠ New ReplicaSet not becoming available — check revision & undo", c["banner_warn"])
    html = html.replace("Context: prod — namespace: catalog", c["context"])

    # First hint
    html = re.sub(
        r'<span class="hint-row-cmd" id="hintCmd"[^>]*>.*?</span>',
        f'<span class="hint-row-cmd" id="hintCmd" title="Click and drag to select, then copy">{c["steps"][0]["hint"]}</span>',
        html,
        count=1,
    )

    return html


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for c in CHALLENGES:
        path = OUT / c["file"]
        path.write_text(build_html(c))
        print(f"Wrote {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
