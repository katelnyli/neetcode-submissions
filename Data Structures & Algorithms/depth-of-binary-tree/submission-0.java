/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public int maxDepth(TreeNode root) {
        return depthHelper(root);
    }

    private int depthHelper(TreeNode curr) {
        if (curr == null) {
            return 0;
        }
        int leftDepth = depthHelper(curr.left);
        int rightDepth = depthHelper(curr.right);
        return Math.max(leftDepth, rightDepth) + 1;
    }

}
