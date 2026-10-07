# Exercise — From my project to our project

Work in pairs. Use GitHub Desktop for repository operations, GitHub web for
invitations and pull requests, and VS Code for editing. Work on your retail
project, outside `pds-materials`.

## Start here: Checkpoint 02

Try your own completed Module 02 project first. From its root, run:

```bash
conda activate pds
python -m pip install -e .
python -m pytest
```

If the tests are green, submit **Checkpoint 02 — Packaging & Testing** in Moodle
as instructed, then keep using your project.

If you are still stuck, download [session-03-start.zip](session-03-start.zip)
and extract `retail-analysis/` into a new location. Keep your old work separately.
Run the same commands from the extracted project root.
**Do not submit the recovery project as your Checkpoint 02 work.**
Use it only to continue with Session 3. Checkpoint 02 should contain your own
Module 02 project. Fix or submit your own M02 work separately according to the
instructor's Moodle instructions.

## Practice stop 1 — Create one shared project

Choose one known-good M02 project as the source of the canonical project
contents. Do not merge the two independent folders. Partner A owns the shared
repository.

### Create the shared repository

1. Partner A opens GitHub in the browser and creates a new repository named
   `retail-analysis` under their account.
2. Make it **PRIVATE** and create it **EMPTY**: do not add a README,
   `.gitignore`, or license. We will bring the project files from M02.

### Clone it

3. In GitHub Desktop, use the clone-repository flow to clone that empty
   repository. Select it from your GitHub repositories, or use its HTTPS URL.
   An empty-repository notice is expected at this point.
4. Note the exact local destination. Choose a new location, separate from the
   old M02 project, and open the clone in VS Code.

### Put the project into the clone

5. In your file manager, copy the **contents** of the known-good M02 folder into
   the clone: README, environment, pyproject, notebook, `data/`, `src/`, and
   `tests/`. **Copy the contents, not the outer `retail-analysis` folder.**
   Keep the clone's own hidden `.git/` directory intact; do not copy any
   `.git/` directory from the old project.

   WRONG:

   ```text
   retail-analysis/          (clone)
     retail-analysis/       (nested old folder)
       src/
       tests/
       pyproject.toml
   ```

   RIGHT:

   ```text
   retail-analysis/          (clone)
     README.md
     environment.yml
     pyproject.toml
     analysis.ipynb
     data/
     src/
     tests/
   ```

6. Create `.gitignore` beside `pyproject.toml` in the clone:

   ```text
   __pycache__/
   .pytest_cache/
   .ipynb_checkpoints/
   *.egg-info/
   ```

   These exclude Python, pytest, notebook caches and generated editable-install
   metadata. Keep `src/`, `tests/`, `pyproject.toml`, `environment.yml`, the
   notebook, README and `data/raw/` in the project history.
7. Confirm GitHub Desktop shows the project files as changes. Review the list:
   generated caches and `egg-info` should be excluded.

### Record the first project state

8. In Desktop, commit the project files and `.gitignore` with the message
   `Initial working project`.
9. Push the commit to the existing GitHub repository. If Desktop offers to
   publish the initial branch, use that action. Check on GitHub web that the
   project files are directly at the repository root and the commit is present.
   The later exercises use `main`; confirm this is the branch you are sharing.

### Add Partner B

10. Partner A invites Partner B through the repository's collaborator/access
    settings on GitHub web.
11. Partner B accepts the invitation, then clones the shared repository with
    GitHub Desktop into a new local folder.
12. Partner B opens the clone in VS Code and runs the following from its root.
    Partner A also runs these commands in A's clone so neither environment
    still points at the old M02 folder:

    ```bash
    conda activate pds
    python -m pip install -e .
    python -m pytest
    ```

    If your existing `pds` environment is missing declared dependencies,
    run `conda env update -f environment.yml` first, then repeat the commands.
    The environment contract has not changed since M02.

Each clone is its own local project. An editable install points Python at a
local folder: install the clone you are using. From now on, **both partners work
only in their clones**. The old M02 folders are backups, not active projects.

**Pause:** both partners can open the private repository and both local clones
pass tests. Continue only when the pair has reached this point.

## Practice stop 2 — Round 1: a README proposal

Partner A proposes; Partner B reviews.

1. In Desktop, select `main`, fetch the remote changes, and pull if updates are
   available. Create a branch such as `docs-running-tests` from this updated
   `main`. Fetch checks for updates; pull brings them into your local branch.
2. In VS Code, add a short `## Running the tests` section to `README.md`, stating
   that `python -m pytest` runs from the project root with `pds` active. If the
   section already exists, clarify that instruction rather than duplicating it.
3. Run the documented command. Review the changed lines in Desktop. Commit with
   a message such as `Document how to run tests`.
4. Publish the branch on its first push, or push its new commits if already
   published. Open a pull request on GitHub web with your branch as the proposal
   and `main` as the destination. Briefly describe the change and your check.
5. Partner B reads the changed lines, checks whether the instructions are usable,
   and leaves a specific comment or approval. For example: "The command states
   both the environment and working directory." Ask for a correction if needed;
   Partner A commits and pushes it on the same branch, updating the same PR.
6. When both agree, Partner B merges the PR on GitHub web.
7. Both switch back to `main` in Desktop, fetch and pull. Verify the new README
   section appears locally. Merging online does not update your laptop for you.

## Practice stop 3 — Round 2: swap roles

Partner B proposes; Partner A reviews.

1. Start from updated `main` and create a branch such as `test-canonical-id`.
2. Add one tiny test to `tests/test_prepare_data.py`: an already canonical ID
   `"C004"` should remain `"C004"`. Use a small Pandas Series and call
   `normalize_ids`. The current implementation already supports this behaviour;
   no helper change or new normalization rule is needed.
3. Run `python -m pytest`. All tests must pass before sharing. Review the diff,
   commit with a meaningful message, then publish/push the branch and open a PR.
4. Partner A inspects the PR diff on GitHub, verifies that the test makes sense,
   and leaves a specific review/comment or approval. Merge when satisfied.
5. Both switch back to `main`, fetch/pull and run `python -m pytest` again.

Optional: the reviewer may also select the proposed branch locally in Desktop
and run `python -m pytest` before merging.

**Pause:** both partners have proposed and reviewed a change. Each can explain
which step saved a file, recorded a local commit, or shared it remotely.

## Instructor demo / optional extension — A conflict

Both branches start from the README line `Retail analysis`. Partner A changes
it to `Retail project`; Partner B changes it to `Retail data analysis`. After
the first is merged, the second may conflict. Watch the instructor inspect both
edits, agree the intended wording, resolve it, and check the result before
completing the merge. Pull the merged result and recheck the project.

> Git can tell you that two changes conflict. Git cannot decide which meaning
> is correct.

Reproduce this only if time remains. Creating or resolving a conflict is not
required for the core checkpoint.

## Checkpoint 03 — Git & Collaboration

Verify that:

- Checkpoint 02 was submitted as instructed, or recovery use was discussed with
  the instructor; the Git exercise began with green tests;
- one shared **private** GitHub repository exists and both partners have working
  local clones;
- the initial working project is recorded and `.gitignore` excludes generated
  local artefacts;
- each partner worked on a branch and practiced both proposer and reviewer roles;
- at least one PR contains a meaningful review and has been merged;
- tests pass on merged `main` after the technical change;
- both understand pull before work, commit locally and push to share.

Prepare the **repository URL** and a **reviewed, merged pull request URL** for
the Checkpoint 03 Moodle submission. The repository history should show both
rounds. This evidence is not another ZIP. Keep the repository private and
provide the instructor access as directed so the links can be reviewed.
