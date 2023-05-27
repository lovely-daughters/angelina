import { transpileModule, ScriptTarget } from "typescript";

function transpileTypeScriptToJavaScript(code: string): string {
    const result = transpileModule(code, {
        compilerOptions: { target: ScriptTarget.ES2018 },
    });
    return result.outputText;
}
