---
layout: default
title: Home
---
# Welcome to DS2002 Data Science Systems!

This repository tracks your working environment during this course. Course materials and tools are distributed through this repository to ensure we all have a common set of tools, scripts, and datasets.

## Getting Started

To get started with the course, please follow the **[Setup Instructions](setup.md)** to configure your development environment.

## Practice

Work through the **[Hands-on Exercises](exercises.md)** to practice and consolidate concepts introduced during class lectures and discussions. 

Each unit contains an "Advanced Concepts" section that allows you to dive deeper into a topic. **Note: Advanced concepts will not be covered in quizzes or labs.**

Check the end of each unit for links to additional resources for further exploration.

## Labs

Weekly labs are released with instructions on the **[course Canvas page](https://canvas.its.virginia.edu/courses/167598)**.

## Repository Management

### Updating Your Fork

To stay current with new releases from the course repository:

1. Add an upstream source (if not already added):
   ```bash
   git remote add upstream git@github.com:nmagee/ds2002-course.git
   ```

2. Fetch from the upstream branch:
   ```bash
   git fetch upstream
   ```

3. Merge your branch with the upstream branch:
   ```bash
   git merge upstream/main main
   ```

### Saving Your Changes

If you generate code, scripts, data files, etc. that you would like to keep, add, commit, and push the files back to **your** fork of the repository:

```bash
git add .
git commit -m "Some meaningful message"
git push origin main
```

Remember that changes you commit and push will be saved to **your** fork of the repository.

