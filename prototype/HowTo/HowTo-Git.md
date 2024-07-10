# HowTo-Git

## Summary
This HowTo goes through using git via the command line.

## Content
- Notes
- Step-by-Step Workflow
- Full Example Workflow
- Clean-up (Optional)

## Notes
For this project it will be best practice to make changes on a branch other than the main branch.
In this case the development branch will often be used and deleted when not needed.

## Step-by-Step Workflow

1. **Ensure You Are on the `development` Branch**:
    ```sh
    git checkout -b development
    ```
The *-b* ensures that the development branch is created locally.

2. **Push Local `development` Branch to Remote**:
    ```sh
    git push -u origin development
    ```

3. **Switch to the `main` Branch**:
    ```sh
    git checkout main
    ```

4. **Update the Local `main` Branch with the Latest Changes**:
    ```sh
    git pull origin main
    ```

5. **Merge the `development` Branch into the `main` Branch**:
    ```sh
    git merge development
    ```

6. **Resolve Any Merge Conflicts (if any)**:
    - Open the conflicting files and resolve the conflicts.
    - After resolving the conflicts, add the resolved files:
      ```sh
      git add <resolved_file>
      ```

    - Continue the merge if you used `git rebase` to resolve conflicts:
      ```sh
      git rebase --continue
      ```

    - If you used `git merge`, commit the merge:
      ```sh
      git commit
      ```

7. **Push the Merged `main` Branch to the Remote Repository**:
    ```sh
    git push origin main
    ```

## Full Example Workflow

Here’s the complete sequence of commands:

1. **Ensure you are on the `development` branch**:
    ```sh
    git checkout -b development
    ```

2. **Push local `development` branch to remote**:
    ```sh
    git push -u origin development
    ```

3. **Switch to the `main` branch**:
    ```sh
    git checkout main
    ```

4. **Update the local `main` branch with the latest changes**:
    ```sh
    git pull origin main
    ```

5. **Merge the `development` branch into the `main` branch**:
    ```sh
    git merge development
    ```

6. **Resolve any merge conflicts (if any)**:
    - Open the conflicting files and resolve the conflicts.
    - After resolving the conflicts, add the resolved files:
      ```sh
      git add <resolved_file>
      ```

    - Commit the merge:
      ```sh
      git commit
      ```

7. **Push the merged `main` branch to the remote repository**:
    ```sh
    git push origin main
    ```

## Clean Up (Optional)

If you no longer need the `development` branch, you can delete it both locally and remotely:

1. **Delete the local `development` branch**:
    ```sh
    git branch -d development
    ```

2. **Delete the remote `development` branch**:
    ```sh
    git push origin --delete development
    ```
