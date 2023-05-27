import { transpileModule, ScriptTarget } from "typescript";

function transpileTypeScriptToJavaScript(code: string): string {
    const result = transpileModule(code, {
        compilerOptions: { target: ScriptTarget.ES2018 },
    });
    return result.outputText;
}

const ts_string = process.argv[2];
if (!ts_string) {
    process.exit(1);
}

const js_string = transpileTypeScriptToJavaScript(ts_string);
console.log(js_string);
