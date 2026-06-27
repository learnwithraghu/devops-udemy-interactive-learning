# Challenge Content Catalog

Video copy and links for every interactive challenge in this repo.  
Add your hosted challenge URL in each **Link** field when ready.

---

## Linux Challenges (6)

### 1. Mis-deployed Artifact

| Field | Content |
|-------|---------|
| **File** | `challenges/lx-filesystem.html` |
| **Short URL** | `/lx-filesystem` |
| **Video heading** | Bad Deploy Hunt |
| **Video title** | Trace a mis-deployed binary across Linux filesystem paths systematically today |
| **Link** | |

**What students might learn**

- Navigate a real server layout with `cd`, `ls`, and `pwd`
- Locate files with `find` and follow symlinks to their targets
- Read metadata with `file`, `stat`, and `readlink` to confirm what is running
- Build a repeatable workflow for tracing a bad release on disk

---

### 2. Linux Server Rescue

| Field | Content |
|-------|---------|
| **File** | `challenges/lx-server-rescue.html` |
| **Short URL** | `/lx-server-rescue` |
| **Video heading** | Server Down Fix |
| **Video title** | Diagnose and restore a production web server under active incident pressure |
| **Link** | |

**What students might learn**

- Check whether a service is listening and responding on the host
- Inspect running processes and recent system logs for failure clues
- Correlate config, ports, and service state before restarting anything
- Practice a calm incident workflow from triage through verification

---

### 3. Log Detective

| Field | Content |
|-------|---------|
| **File** | `challenges/lx-log-detective.html` |
| **Short URL** | `/lx-log-detective` |
| **Video heading** | Log Detective |
| **Video title** | Investigate overnight application failures using Linux log analysis before standup |
| **Link** | |

**What students might learn**

- Find the right log files and sort them by recency
- Filter noisy logs down to errors in a specific time window
- Read stack traces and error messages to narrow the blast radius
- Count and rank error types to explain impact to stakeholders

---

### 4. Permission Fix Lab

| Field | Content |
|-------|---------|
| **File** | `challenges/lx-permissions.html` |
| **Short URL** | `/lx-permissions` |
| **Video heading** | Fix Permissions |
| **Video title** | Fix broken file modes and ownership on shared deploy path |
| **Link** | |

**What students might learn**

- Interpret `ls -l` and `ls -ld` output for files and directories
- Adjust execute bits and numeric modes with `chmod` safely
- Align ownership with the service account using `chown` and `groups`
- Verify defaults with `umask` and confirm the final state before handoff

---

### 5. Pipeline & Text Workshop

| Field | Content |
|-------|---------|
| **File** | `challenges/lx-pipelines.html` |
| **Short URL** | `/lx-pipelines` |
| **Video heading** | Text Pipelines |
| **Video title** | Master Unix text tool pipelines on CSV exports and logs |
| **Link** | |

**What students might learn**

- Preview and measure data with `head`, `tail`, and `wc`
- Extract and reshape fields using `cut`, `sort`, and `uniq`
- Filter job output with `grep` and summarize columns with `awk`
- Chain commands through classic `sort | uniq -c | sort -rn` patterns

---

### 6. Disk Watch

| Field | Content |
|-------|---------|
| **File** | `challenges/lx-disk-space.html` |
| **Short URL** | `/lx-disk-space` |
| **Video heading** | Disk Space Triage |
| **Video title** | Hunt disk space hogs on var with df du and find |
| **Link** | |

**What students might learn**

- Confirm filesystem pressure with `df -h` and focus on the right mount
- Drill into heavy directories under `/var` and `/var/log` with `du`
- Surface oversized or stale files using pipes and `find`
- Practice a safe discovery workflow before deleting or rotating anything

---

## Docker Challenges (2)

### 7. Anonymous Exit

| Field | Content |
|-------|---------|
| **File** | `challenges/docker/dc-anonymous-exit.html` |
| **Short URL** | — (no short URL in `_redirects` yet) |
| **Video heading** | Exit Code 127 |
| **Video title** | Debug Docker container exiting immediately with mysterious exit code 127 |
| **Link** | |

**What students might learn**

- Inspect container state and exit codes with `docker ps` and `docker inspect`
- Read container logs to see what failed before the process died
- Understand how `ENTRYPOINT`, `CMD`, and shell scripts interact at startup
- Trace missing binaries, bad paths, and permission issues in images

---

### 8. Isolated Service

| Field | Content |
|-------|---------|
| **File** | `challenges/docker/dc-isolated-service.html` |
| **Short URL** | — (no short URL in `_redirects` yet) |
| **Video heading** | Container Networking |
| **Video title** | Diagnose why Docker containers on the same network cannot communicate |
| **Link** | |

**What students might learn**

- Inspect bridge networks and attached containers with `docker network inspect`
- Test reachability from inside a container using `docker exec`, `ping`, and `curl`
- Verify port mappings and the hostnames apps are configured to use
- Read `Dockerfile` and Compose network settings that affect service discovery

---

## Kubernetes Challenges (5)

### 9. Config Mount

| Field | Content |
|-------|---------|
| **File** | `challenges/k8/k8-config-mount.html` |
| **Short URL** | `/k8-config-mount` |
| **Video heading** | ConfigMap Mismatch |
| **Video title** | Debug Kubernetes ConfigMap mounts when applications read the wrong files |
| **Link** | |

**What students might learn**

- Read volume mounts and projected paths from `kubectl describe pod`
- Compare ConfigMap keys and filenames the application expects on disk
- Use `kubectl logs` to spot file-not-found and parse errors at startup
- Trace miswired chart values back to the Deployment volume definition

---

### 10. CrashLoopBackOff

| Field | Content |
|-------|---------|
| **File** | `challenges/k8/k8-pod-restart-loop.html` |
| **Short URL** | `/k8-pod-restart-loop` |
| **Video heading** | CrashLoopBackOff |
| **Video title** | Trace Kubernetes CrashLoopBackOff failures using describe logs and events |
| **Link** | |

**What students might learn**

- List pods and read scheduling status with `kubectl get`
- Pull events and container state from `kubectl describe pod`
- Compare current and previous logs to see why the container exits
- Correlate pod failures with Deployment image and rollout history

---

### 11. Resource Pressure

| Field | Content |
|-------|---------|
| **File** | `challenges/k8/k8-resource-pressure.html` |
| **Short URL** | `/k8-resource-pressure` |
| **Video heading** | OOMKilled Pressure |
| **Video title** | Investigate Kubernetes OOMKilled pods using top describe and node metrics |
| **Link** | |

**What students might learn**

- Rank noisy pods and nodes with `kubectl top`
- Read requests, limits, and last terminated state from `describe pod`
- Inspect node allocatable capacity and pressure conditions
- Connect cluster events to memory exhaustion and CPU throttling symptoms

---

### 12. Rollout Stuck

| Field | Content |
|-------|---------|
| **File** | `challenges/k8/k8-rollout-stuck.html` |
| **Short URL** | `/k8-rollout-stuck` |
| **Video heading** | Stuck Rollout |
| **Video title** | Unblock a stuck Kubernetes deployment rollout and roll back safely |
| **Link** | |

**What students might learn**

- Check Deployment health and progress with `kubectl rollout status`
- Compare ReplicaSets and revision numbers after a bad release
- Read pod failure details from `describe` and the image field
- Use rollout history and undo to restore a known-good revision

---

### 13. Service Blind Spot

| Field | Content |
|-------|---------|
| **File** | `challenges/k8/k8-service-blind-spot.html` |
| **Short URL** | `/k8-service-blind-spot` |
| **Video heading** | Empty Endpoints |
| **Video title** | Fix Kubernetes service 502 errors when endpoints never populate correctly |
| **Link** | |

**What students might learn**

- Inspect Services and Endpoints together in a live namespace
- Compare Service selectors against the labels on running pods
- Use label queries (`-l`) to see which pods a Service should route to
- Understand why healthy pods can still leave a Service with no backends

---

## Quick Reference

| # | Track | Challenge | Video heading | Short URL |
|---|-------|-----------|---------------|-----------|
| 1 | Linux | Mis-deployed Artifact | Bad Deploy Hunt | `/lx-filesystem` |
| 2 | Linux | Server Rescue | Server Down Fix | `/lx-server-rescue` |
| 3 | Linux | Log Detective | Log Detective | `/lx-log-detective` |
| 4 | Linux | Permission Fix Lab | Fix Permissions | `/lx-permissions` |
| 5 | Linux | Pipeline Workshop | Text Pipelines | `/lx-pipelines` |
| 6 | Linux | Disk Watch | Disk Space Triage | `/lx-disk-space` |
| 7 | Docker | Anonymous Exit | Exit Code 127 | — |
| 8 | Docker | Isolated Service | Container Networking | — |
| 9 | K8s | Config Mount | ConfigMap Mismatch | `/k8-config-mount` |
| 10 | K8s | CrashLoopBackOff | CrashLoopBackOff | `/k8-pod-restart-loop` |
| 11 | K8s | Resource Pressure | OOMKilled Pressure | `/k8-resource-pressure` |
| 12 | K8s | Rollout Stuck | Stuck Rollout | `/k8-rollout-stuck` |
| 13 | K8s | Service Blind Spot | Empty Endpoints | `/k8-service-blind-spot` |

**Total: 13 challenges** — 6 Linux · 2 Docker · 5 Kubernetes
