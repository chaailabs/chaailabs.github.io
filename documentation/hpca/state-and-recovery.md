# State and recovery

HPCA separates desired workflow state from scheduler state and filesystem evidence. On restart it reconciles all three before submitting work.

Recovery follows a fixed sequence: validate configuration, inspect durable state, query the scheduler, verify artifacts, classify the failure, apply an authorized correction, and resume from the earliest invalid stage. Completed valid artifacts are preserved.

Retries are bounded. Repeated failure becomes an explicit blocked state rather than an infinite submission loop.

