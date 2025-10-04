import * as vscode from 'vscode';
import axios from 'axios';

export function activate(context: vscode.ExtensionContext) {
    console.log('EvoCode AI extension is now active!');
    
    let aiEnabled = vscode.workspace.getConfiguration('evocode').get('enableAI', true);
    let collaborationEnabled = vscode.workspace.getConfiguration('evocode').get('collaborationEnabled', true);
    
    const startSessionCommand = vscode.commands.registerCommand('evocode.startSession', async () => {
        if (!collaborationEnabled) {
            vscode.window.showWarningMessage('Collaboration features are disabled. Enable in settings.');
            return;
        }
        
        const sessionName = await vscode.window.showInputBox({
            prompt: 'Enter session name for collaboration',
            placeHolder: 'My Coding Session'
        });
        
        if (sessionName) {
            vscode.window.showInformationMessage(`Starting EvoCode session: ${sessionName}`);
            
            try {
                const response = await createCollaborationSession(sessionName);
                vscode.window.showInformationMessage(`Session created: ${response.sessionId}`);
            } catch (error) {
                vscode.window.showErrorMessage('Failed to create collaboration session');
            }
        }
    });
    
    const suggestEvolutionCommand = vscode.commands.registerCommand('evocode.suggestEvolution', async () => {
        const suggestion = await vscode.window.showInputBox({
            prompt: 'Suggest a feature evolution for EvoCode AI',
            placeHolder: 'Describe your feature idea...'
        });
        
        if (suggestion) {
            vscode.window.showInformationMessage('Evolution suggestion recorded! The community will vote on this.');
            
            try {
                await submitEvolutionSuggestion(suggestion);
            } catch (error) {
                vscode.window.showErrorMessage('Failed to submit evolution suggestion');
            }
        }
    });
    
    const viewMetricsCommand = vscode.commands.registerCommand('evocode.viewMetrics', async () => {
        try {
            const metrics = await getAIMetrics();
            
            const panel = vscode.window.createWebviewPanel(
                'evocodeMetrics',
                'EvoCode AI Metrics',
                vscode.ViewColumn.One,
                {}
            );
            
            panel.webview.html = getMetricsWebviewContent(metrics);
        } catch (error) {
            vscode.window.showErrorMessage('Failed to load AI metrics');
        }
    });
    
    if (aiEnabled) {
        setupAICompletion(context);
    }
    
    context.subscriptions.push(
        startSessionCommand,
        suggestEvolutionCommand,
        viewMetricsCommand
    );
}

function setupAICompletion(context: vscode.ExtensionContext) {
    const provider = vscode.languages.registerCompletionItemProvider(
        { scheme: 'file', language: 'python' },
        {
            provideCompletionItems(document: vscode.TextDocument, position: vscode.Position) {
                const linePrefix = document.lineAt(position).text.substr(0, position.character);
                
                const completions: vscode.CompletionItem[] = [];
                
                if (linePrefix.endsWith('def ')) {
                    const functionCompletion = new vscode.CompletionItem('function_template', vscode.CompletionItemKind.Snippet);
                    functionCompletion.insertText = new vscode.SnippetString('${1:function_name}(${2:params}):\n\t"""${3:docstring}"""\n\t${4:pass}');
                    functionCompletion.documentation = new vscode.MarkdownString('EvoCode AI: Function template');
                    completions.push(functionCompletion);
                }
                
                if (linePrefix.endsWith('class ')) {
                    const classCompletion = new vscode.CompletionItem('class_template', vscode.CompletionItemKind.Snippet);
                    classCompletion.insertText = new vscode.SnippetString('${1:ClassName}:\n\tdef __init__(self${2:, params}):\n\t\t${3:pass}');
                    classCompletion.documentation = new vscode.MarkdownString('EvoCode AI: Class template');
                    completions.push(classCompletion);
                }
                
                return completions;
            }
        },
        ' ' // triggered by space
    );
    
    context.subscriptions.push(provider);
}

async function createCollaborationSession(sessionName: string): Promise<any> {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve({
                sessionId: `session_${Date.now()}`,
                name: sessionName,
                participants: 1
            });
        }, 1000);
    });
}

async function submitEvolutionSuggestion(suggestion: string): Promise<void> {
    console.log('Evolution suggestion submitted:', suggestion);
    return Promise.resolve();
}

async function getAIMetrics(): Promise<any> {
    return {
        aiAccuracy: 0.85,
        learningRate: 0.1,
        suggestionsProvided: 1247,
        userSatisfaction: 4.2
    };
}

function getMetricsWebviewContent(metrics: any): string {
    return \`
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body { font-family: Arial, sans-serif; padding: 20px; }
                .metric { margin: 10px 0; padding: 10px; background: #f5f5f5; border-radius: 5px; }
                .value { font-weight: bold; color: #2ea44f; }
            </style>
        </head>
        <body>
            <h1>EvoCode AI Metrics</h1>
            <div class="metric">AI Accuracy: <span class="value">\${(metrics.aiAccuracy * 100).toFixed(1)}%</span></div>
            <div class="metric">Learning Rate: <span class="value">\${metrics.learningRate}</span></div>
            <div class="metric">Suggestions Provided: <span class="value">\${metrics.suggestionsProvided}</span></div>
            <div class="metric">User Satisfaction: <span class="value">\${metrics.userSatisfaction}/5</span></div>
        </body>
        </html>
    \`;
}

export function deactivate() {}
