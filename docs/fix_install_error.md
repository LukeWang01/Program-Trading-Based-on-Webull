### 1. Error: Installing error for `simpleaduio` on Windows:

If you got errors to install the `simpeaudio` library, you can try the following steps:

1.  Go to https://visualstudio.microsoft.com/visual-cpp-build-tools/
2.  Download the C++ Build Tools Installer
3.  Run the installer and install the C++ Build Tools

After install, try:

```
pip install simpleaudio
```

or,

```
pip install -r requirements.txt
```

or,

```
pip3 install -r requirements.txt
```

<br>

![5704e8798a0e1bcffb39208c781765e](docs_img/install_vc_1.png)

![5704e8798a0e1bcffb39208c781765e](docs_img/install_vc_2.png)


<br>

### 2. Error: Installing `lxml` error on MacOS:

If you got the error when installing `lxml`:

The error you're encountering indicates that the `lxml` library is having trouble building because it's missing some dependencies and the required developer tools.

Here's a step-by-step guide to resolve this issue:

1. **Install Xcode Command Line Tools:**

   Open your terminal and run the following command to install Xcode Command Line Tools:

   ```bash
   xcode-select --install
   ```

   Follow the on-screen prompts to complete the installation.

2. **Install Homebrew:**

   If you don't have Homebrew installed, you can install it using the following command:

   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
   ```

3. **Install Required Dependencies:**

   Use Homebrew to install the necessary dependencies for `lxml`:

   ```bash
   brew install libxml2
   brew install libxslt
   ```

4. **Set Environment Variables:**

   Set the environment variables required for `lxml` to locate the dependencies correctly. Add these lines to your shell profile file (e.g., `~/.zshrc`):

   ```bash
   export CFLAGS="-I/usr/local/opt/libxml2/include -I/usr/local/opt/libxslt/include"
   export LDFLAGS="-L/usr/local/opt/libxml2/lib -L/usr/local/opt/libxslt/lib"
   ```

   Then, run the following command to apply the changes:

   ```bash
   source ~/.zshrc
   ```

5. **Retry Installation:**

   Now, try installing `lxml` again using `pip`:

   ```bash
   pip install lxml
   ```

With these steps, you should be able to successfully install `lxml`. 

After installation, try:

`pip install simpleaudio`

or,

`pip install -r requirements.txt`

or,

`pip3 install -r requirements.txt`

<br>
