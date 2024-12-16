# Angelina

This is a custom jupyter kernel tailored for vanilla-js web development (chrome extensions are my specific usecase).

Jupyter notebooks are a huge timesaver that allow me to iteratively build up solutions.

I would like to extend this idea to the browser where I can remotely hook up a notebook to chrome and work through that in vscode.

I've tried reading js files as a string and passing that through selenium to chrome, but I have to develop in a separate file & variables aren't saved.

I've tried the ijavascript kernel paired with chrome-remote-interface, however that experience was extremely janky.

AFAIK, there isn't anything that works, so this is my attempt to create one.

https://chromedevtools.github.io/devtools-protocol/tot/Runtime/#method-evaluate
userGesture - Whether execution should be treated as initiated by user in the UI.
replMode - Setting this flag to true enables let re-declaration and top-level await. Note that let variables can only be re-declared if they originate from replMode themselves. EXPERIMENTAL

userGesture allows persistence of declarations
replMode allows const/let redeclaration which is an essential part of the notebook experience

```
# Installing kernel
jupyter kernelspec install ./angelina_kernel/kernelspec --replace --name angelina
jupyter kernelspec list
jupyter notebook

# Starting browser in remote debug mode
"Google Chrome" --remote-debugging-port=9222
```
